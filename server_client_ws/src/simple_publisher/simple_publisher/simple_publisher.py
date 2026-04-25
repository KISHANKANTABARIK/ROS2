import rclpy
from rclpy.node import Node
from custom_interfaces.msg import HardwareInterface
# from example_interfaces.msg import String

class SimplePublisher(Node):
    def __init__(self):
        super().__init__("SimplePublisher")
        self.publish = self.create_publisher(HardwareInterface, "/motor_status", 10)
        
        self.create_timer(1.0, self.send_status)
        self.get_logger().info("The SimplePublisher is starting")

    def send_status(self):
        motor_status = HardwareInterface()

        motor_status.temp = 25.0
        motor_status.motor_status = True
        motor_status.debug_message = "Motor is on"
        self.publish.publish(motor_status)


        

def main():
    rclpy.init()
    node = SimplePublisher()
    rclpy.spin(node)
    rclpy.shutdown()