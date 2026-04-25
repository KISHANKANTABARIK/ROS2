import rclpy
from rclpy.node import Node
from example_interfaces.msg import Float64

class HumiditySensor(Node):
    def __init__(self):
        super().__init__("humidity_sensor")
        
        self.humidity =40
        self.publisher = self.create_publisher(Float64, "/home/humidity", 10)
        self.create_timer(2.0,self.send_data)

    def send_data(self):
        msg = Float64() 

        msg.data = float(self.humidity)

        self.publisher.publish(msg)
        
        if(self.humidity==80):
            self.humidity = 40
        self.get_logger().info(f"Humidity {self.humidity}")
        self.humidity += 5
def main():
    rclpy.init()
    humidity_sensor = HumiditySensor()
    rclpy.spin(humidity_sensor)
    rclpy.shutdown()