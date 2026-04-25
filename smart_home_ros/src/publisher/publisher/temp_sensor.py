import rclpy
from rclpy.node import Node
from example_interfaces.msg import Float64

class TempSensor(Node):
    def __init__(self):
        super().__init__("temp_sensor")
        
        self.temperature =20
        self.publisher = self.create_publisher(Float64, "/home/temperature", 10)
        self.create_timer(1.0,self.send_data)

    def send_data(self):
        msg = Float64() 

        msg.data = float(self.temperature)

        self.publisher.publish(msg)
        
        if(self.temperature>=35):
            self.temperature = 20
        self.get_logger().info(f"Temperature {self.temperature}")
        self.temperature += 1
def main():
    rclpy.init()
    temp_sensor = TempSensor()
    rclpy.spin(temp_sensor)
    rclpy.shutdown()