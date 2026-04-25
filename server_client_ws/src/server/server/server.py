import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

class Server(Node):
    
    def __init__(self):
        super().__init__("server")

        self.server = self.create_service(AddTwoInts, "/add_two_ints", self.call_srvice)

        self.get_logger().info("Add two ints server started")

    def call_srvice(self, request: AddTwoInts.Request, response: AddTwoInts.Response):

        # response = AddTwoInts.Response()
        response.sum = request.a+ request.b

        self.get_logger().info(f"Sum: {request.a} + {request.b} = {response.sum}")

        return response

def main():
    rclpy.init()
    server = Server()
    rclpy.spin(server)
    rclpy.shutdown()
