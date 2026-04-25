import rclpy
from rclpy.node import Node
from coustom_interfaces.srv import MotorTemp

class StatusClient(Node):
    def __init__(self):
        super().__init__("status_client")

        self.client_ = self.create_client(MotorTemp, "/update_temp")
        self.get_logger().info("Client started")

    def update_temp(self, temperature):

        request = MotorTemp.Request()
        request.temperature = temperature

        future = self.client_.call_async(request)
        rclpy.spin_until_future_complete(self,future)
        response = future.result()

        if response.success:
            self.get_logger().info("Motor is On")
        else:
            self.get_logger().info("Motor is Off")

def main():
    rclpy.init()
    status_client = StatusClient()
    status_client.update_temp(35.0)
    rclpy.spin(status_client)
    rclpy.shutdown()