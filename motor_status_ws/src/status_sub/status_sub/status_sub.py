import rclpy
from rclpy.node import Node
from coustom_interfaces.msg import HardwareStatus
import time

class StatusSub(Node):
    def __init__(self):
        super().__init__("status_sub")

        self.status_sub = self.create_subscription(HardwareStatus, "/motor_status", self.reciev_data, 10)

    def reciev_data(self, msg):
       
        self.get_logger().info(f"Temperature is {msg.temperature}")
        self.get_logger().info(f"Motor Status is {msg.motor_status}")
        self.get_logger().info(f"Debug message is {msg.debug_message}")

        time.sleep(1.0)

def main():
    rclpy.init()
    node = StatusSub()
    rclpy.spin(node)
    rclpy.shutdown()