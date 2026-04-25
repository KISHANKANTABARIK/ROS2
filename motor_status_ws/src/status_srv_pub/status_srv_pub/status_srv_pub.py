import rclpy
from rclpy.node import Node
from coustom_interfaces.msg import HardwareStatus
from coustom_interfaces.srv import MotorTemp

class StatusSrvPub (Node):
    def __init__(self):
        super().__init__("status_srv_pub")

        self.temperature = 25.0
        self.motor_status = False
        self.debug_message = "Motor is On"

        self.server = self.create_service(MotorTemp, "/update_temp", self.call_temp_status_server)
        self.get_logger().info("status server is started")

        self.status_publishers = self.create_publisher(HardwareStatus, "/motor_status", 10)
        self.create_timer(1.0, self.publish_motor_status)
        self.get_logger().info("status publisher is started")


    def call_temp_status_server(self, request: MotorTemp.Request, response: MotorTemp.Response):
        self.temperature = request.temperature

        if (request.temperature > 30):
            self.get_logger().info("Temperature is High")
            response.success = False
            self.motor_status = False
            self.debug_message = "Motor is Off"

        else :
            self.get_logger().info("Temperature is Low")
            response.success = True
            self.motor_status = True
            self.debug_message = "Motor is No"

        self.get_logger().info(f"The motore temp is {request.temperature} > 30 {response.success}")

        return response
    
    def publish_motor_status(self):
        motor_status = HardwareStatus()

        motor_status.temperature = self.temperature
        motor_status.motor_status = self.motor_status
        motor_status.debug_message = self.debug_message

        self.status_publishers.publish(motor_status)

def main():
    rclpy.init()
    server = StatusSrvPub()
    rclpy.spin(server)
    rclpy.shutdown()