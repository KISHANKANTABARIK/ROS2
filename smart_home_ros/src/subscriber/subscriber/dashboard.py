import rclpy
from rclpy.node import Node
from example_interfaces.msg import Float64, Bool

class Dashboard(Node):
    def __init__(self):
        super().__init__("dashboard")

        self.get_logger().info("======= Smart Home Dashboard =======")

        # Store values
        self.temperature = 0.0
        self.humidity = 0.0
        self.motion = False

        # Subscriptions
        self.create_subscription(Float64, "/home/temperature", self.temp_callback, 10)
        self.create_subscription(Float64, "/home/humidity", self.humidity_callback, 10)
        self.create_subscription(Bool, "/home/motion", self.motion_callback, 10)

        # Timer for dashboard display
        self.create_timer(2.0, self.display_dashboard)

    def temp_callback(self, msg):
        self.temperature = msg.data

    def humidity_callback(self, msg):
        self.humidity = msg.data

    def motion_callback(self, msg):
        self.motion = msg.data

    def display_dashboard(self):
        self.get_logger().info("\n====== Smart Home Dashboard ======")
        self.get_logger().info(f"Temperature : {self.temperature:.2f} C")
        self.get_logger().info(f"Humidity    : {self.humidity:.2f} %")
        self.get_logger().info(f"Motion      : {'DETECTED' if self.motion else 'NONE'}")
        self.get_logger().info("=================================\n")


def main():
    rclpy.init()
    node = Dashboard()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()