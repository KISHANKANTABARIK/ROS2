import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64

# from std_msgs.msg import String

class OnePublisher(Node): # Ctrl+ click on Node to get the all Method exist in the class Node

    def __init__(self):
        super().__init__("one_publisher") # Node name - "one_publisher"

        self.counter =  0
        self.one_publisher = self.create_publisher(Int64, "/counter", 10)
        #                       function to publish (msg_type, topic to publish, qos_profile)

        # self.one_publisher = self.create_publisher(String, "/counter", 10)

        self.create_timer(0.1, self.send_data) # "self.send_data" it is a callback - a method which class another method in it 
        self.get_logger().info(f"NUmber Publisher has been started")

    def send_data(self):
        msg = Int64() #creating an object for the class Int64
        #msg = String() # Topics and message is msg  Type
                       # Request and response - Service and client (srv)
        # msg.data = f"Hello {self.counter}"

        msg.data = self.counter

        self.one_publisher.publish(msg) # We are publishing the object not the data , the data is inside of that object
        self.counter += 1

        self.get_logger().info(f"Hello {self.counter}")


def main():
    rclpy.init()
    one_publisher = OnePublisher()
    rclpy.spin(one_publisher)
    one_publisher.destroy_node()
    rclpy.shutdown()
        

        