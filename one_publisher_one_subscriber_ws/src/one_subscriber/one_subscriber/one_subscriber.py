import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64

#18/03
import time

class OneSubscriber(Node):
    def __init__(self):
        super().__init__("one_subscriber") #Node name - one_subscriber

        
        self.one_subscriber = self.create_subscription(Int64, "/counter",self.reciev_data,10)
        #                          function to subscribe (msg_type, subscribed_topic, callback, qos_profile )
        
    def reciev_data(self,msg):
        self.get_logger().info(f"{msg.data}")

        #18/03
        time.sleep(1.0)

def main():
    rclpy.init()
    node = OneSubscriber()
    rclpy.spin(node)
    rclpy.shutdown()