import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
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

    # ── Paths ──────────────────────────────────────────────────────────────
    urdf_path          = os.path.join(pkg_description, 'urdf',   'my_robot.urdf.xacro')
    gazebo_config_path = os.path.join(pkg_bringup,     'config', 'gazebo_bridge.yaml')
    rviz_config_path   = os.path.join(pkg_description, 'rviz',   'urdf_config.rviz')
    world_path         = os.path.join(pkg_bringup,     'worlds', 'robot_world.sdf')

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
    # 7. ROSBridge WebSocket
    # websocket_node = IncludeLaunchDescription(
    #     XMLLaunchDescriptionSource(
    #         os.path.join(pkg_websocket, 'launch', 'rosbridge_websocket_launch.xml')
    #     ),
    #     launch_arguments={'port': '9080'}.items()
    # )

    return LaunchDescription([
        declare_use_sim_time_cmd,
        robot_state_publisher_node,
        gazebo_sim,
        spawn_robot_node,
        bridge_node,
        rviz_node,
        # websocket_node,
    ])
