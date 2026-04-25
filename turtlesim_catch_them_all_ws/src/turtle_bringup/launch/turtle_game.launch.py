from launch_ros.actions import Node
from launch import LaunchDescription

def generate_launch_description():

    turtlesim_package = Node(
        package="turtlesim",
        executable="turtlesim_node"
    )

    turtle_controller_package = Node(
        package="turtle_controller",
        executable="turtle_controller"
    )

    spawner_package = Node(
        package="spawner",
        executable="spawner"
    )

    return LaunchDescription([
        turtlesim_package,
        spawner_package,
        turtle_controller_package
    ])

