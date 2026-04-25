from launch_ros.actions import Node
from launch import LaunchDescription

def generate_launch_description():

    publisher_temp_sensor_package = Node(
        package="publisher",
        executable="temp_sensor"
    )

    publisher_humidity_sensor = Node(
        package="publisher",
        executable="humidity_sensor"
    )

    publisher_motion_sensor = Node(
        package="publisher",
        executable="motion_sensor"
    )

    subscriber_package = Node(
        package="subscriber",
        executable="dashboard"
    )

    return LaunchDescription([
        publisher_temp_sensor_package,
        publisher_humidity_sensor,
        publisher_motion_sensor,
        subscriber_package
    ])

