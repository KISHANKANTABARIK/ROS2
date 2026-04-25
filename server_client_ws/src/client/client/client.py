import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

class Client(Node):
    
    def __init__(self):
        super().__init__("client")

        self.client_ = self.create_client(AddTwoInts, "/add_two_ints")
        self.get_logger().info("client started")

    def start_client(self, a, b):
        
        if(not self.client_.wait_for_service(1.0)):
            self.get_logger().warn("Server is not running")
        

        request = AddTwoInts.Request()

        request.a = a
        request.b = b

        future = self.client_.call_async(request)

        rclpy.spin_until_future_complete(self, future)

        response = future.result()

        self.get_logger().info(f"{request.a} + {request.b} = {response.sum}")

    
def main():
    rclpy.init()
    client = Client()
    client.start_client(4,3)
    rclpy.spin(client)
    rclpy.shutdown()