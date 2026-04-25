import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int32
import time

class MicroROSEsp(Node):
    def __init__(self):
        super().__init__("micro_ros") #Node name - one_subscriber

        
        self.one_subscriber = self.create_subscription(Int32, "/esp32_pub",self.reciev_data,10)
        #                          function to subscribe (msg_type, subscribed_topic, callback, qos_profile )
        
    def reciev_data(self,msg):
        self.get_logger().info(f"{msg.data}")

        #18/03
        time.sleep(1.0)

def main():
    rclpy.init()
    node = MicroROSEsp()
    rclpy.spin(node)
    rclpy.shutdown()

    