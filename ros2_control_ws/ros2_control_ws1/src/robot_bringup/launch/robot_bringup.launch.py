import os
from ament_index_python.packages import get_package_share_directory, get_package_prefix
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, SetEnvironmentVariable
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
import xacro

def generate_launch_description():

    # ── Launch Arguments ───────────────────────────────────────────────────
    declare_use_sim_time_cmd = DeclareLaunchArgument(
        name='use_sim_time',
        default_value='true',
        description='Use simulation (Gazebo) clock if true'
    )
    use_sim_time = LaunchConfiguration('use_sim_time', default='true')

    # ── Package Directories ────────────────────────────────────────────────
    pkg_description  = get_package_share_directory('robot_description')
    pkg_bringup      = get_package_share_directory('robot_bringup')
    pkg_ros_gz_sim   = get_package_share_directory('ros_gz_sim')
    # pkg_websocket    = get_package_share_directory('rosbridge_server')

    gz_ros2_control_prefix = get_package_prefix('gz_ros2_control')
    gz_ros2_control_lib = os.path.join(gz_ros2_control_prefix, 'lib')

    # ── Paths ──────────────────────────────────────────────────────────────
    urdf_path          = os.path.join(pkg_description, 'urdf',   'robot.xacro')
    gazebo_config_path = os.path.join(pkg_bringup,     'config', 'gazebo_bridge.yaml')
    rviz_config_path   = os.path.join(pkg_description, 'rviz',   'robot.rviz')
    world_path         = os.path.join(pkg_bringup,     'worlds', 'world.sdf')

    # ── Process URDF (xacro → XML string) ─────────────────────────────────
    robot_description_config = xacro.process_file(urdf_path)
    robot_description = {'robot_description': robot_description_config.toxml()}

    # ── Nodes ──────────────────────────────────────────────────────────────

    # 1. Robot State Publisher
    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[robot_description, {'use_sim_time': use_sim_time}]
    )

    # 2. Gazebo Sim
    gazebo_sim = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_ros_gz_sim, 'launch', 'gz_sim.launch.py')
        ),
        launch_arguments={
            'gz_args': f'-r {world_path}'
        }.items()
    )

    # 3. Spawn Robot into Gazebo
    spawn_robot_node = Node(
        package='ros_gz_sim',
        executable='create',
        output='screen',
        arguments=['-topic', 'robot_description'],
        parameters=[{'use_sim_time': use_sim_time}]
    )

    # 4. ROS ↔ Gazebo Bridge
    bridge_node = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        output='screen',
        parameters=[
            {'config_file': gazebo_config_path},
            {'use_sim_time': use_sim_time}
        ]
    )

    # 5. RViz2
    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        output='screen',
        arguments=['-d', rviz_config_path],
        parameters=[{'use_sim_time': use_sim_time}]
    )

    #6. Controller Spawner
    joint_state_broadscaster_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["joint_state_broadcaster", "--controller-manager", "/controller_manager"],
    )

    simple_velocity_controller_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["simple_velocity_controller", "--controller-manager", "/controller_manager"],
    )

    # robot_controller_spawner = Node(
    #     package="controller_manager",
    #     executable="spawner",
    #     arguments=["robot_controller", "--controller-manager", "/controller_manager"],
    # )

    #7 set Env variable for gz plagins
    set_gz_plugin_path = SetEnvironmentVariable(
        name='GZ_SIM_PLUGIN_PATH',
        value=[gz_ros2_control_lib, ':', os.environ.get('GZ_SIM_PLUGIN_PATH', '')]
    )

    return LaunchDescription([
        
        set_gz_plugin_path,
        # robot_controller_spawner,
        gazebo_sim,
        simple_velocity_controller_spawner,
        joint_state_broadscaster_spawner,
        declare_use_sim_time_cmd,
        robot_state_publisher_node,
        spawn_robot_node,
        bridge_node,
        rviz_node,
    ])
