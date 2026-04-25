import rclpy
from rclpy.node import Node
from example_interfaces.msg import Bool

class MotionSensor(Node):
    def __init__(self):
        super().__init__("motion_sensor")
        
        self.motion = True
        self.publisher = self.create_publisher(Bool, "/home/motion", 10)
        self.create_timer(3.0,self.send_data)

    def send_data(self):
        msg = Bool() 

        msg.data = self.motion

        self.publisher.publish(msg)
        
        if(self.motion==True):
            self.motion = False
        else:
            self.motion = True
        self.get_logger().info(f"Motion {self.motion}")
        
def main():
    rclpy.init()
    motion_sensor = MotionSensor()
    rclpy.spin(motion_sensor)
    rclpy.shutdown()