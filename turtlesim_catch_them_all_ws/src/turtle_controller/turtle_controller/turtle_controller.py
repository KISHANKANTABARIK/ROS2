import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from turtlesim.srv import Kill
from turtle_interface.srv import CatchTurtle
from turtle_interface.msg import Turtle, TurtleArray
import math

class TurtleController(Node):
    def __init__(self):
        super().__init__("turtle_controller")

        self.master_turtle_pose = Pose()
        self.spawn_turtle_pose = Pose()
        self.turtle_array = []
        

        self.path_publish_1 = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)
        self.create_subscription(Pose, "/turtle1/pose", self.callback_master_turtle,10)
        self.create_subscription(TurtleArray, "/turtle_array", self.callback_spawn_turtle,10)

        self.kill_client = self.create_client(Kill, "/kill")
        self.remove_turtle = self.create_client(CatchTurtle, "/catch_turtle")

        self.create_timer(0.10,self.controller)
        self.get_logger().info("The turtle_controller is started")
    
    def callback_spawn_turtle(self, spawn_pose: TurtleArray):
        self.turtle_array = spawn_pose.turtle_array

    def callback_master_turtle(self, master_pose: Pose):
        self.master_turtle_pose = master_pose

    def controller(self):

        while(not self.kill_client.wait_for_service(1.0)):
            self.get_logger().warn("Kill Service is not Activate")
        
        if(self.turtle_array):
            self.turtle: Turtle = self.turtle_array[0]
            # self.print= self.turtle_array[0]

            # self.get_logger().info(f"{self.print}")
                
            x1 = self.master_turtle_pose.x
            x2 = self.turtle.x
            y1 = self.master_turtle_pose.y
            y2 = self.turtle.y
            theta_1 = self.master_turtle_pose.theta

            distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

            opp = (y2 - y1)
            adj = (x2 - x1)
            angle = math.atan2(opp, adj)

            ang_error = angle - theta_1

            if (ang_error > math.pi):
                ang_error = ang_error - (2 * math.pi)
            elif(ang_error < -math.pi):
                ang_error = ang_error + (2 * math.pi)

            

            send_goal = Twist()
            send_goal.linear.x =  1.5 * distance
            send_goal.angular.z =  6 * ang_error
            

            if(distance<0.5):
                send_goal.linear.x = 0.0
                send_goal.angular.z = 0.0
                
                turtle_remove_req = CatchTurtle.Request()
                turtle_remove_req.name = self.turtle.name
                future_remove = self.remove_turtle.call_async(turtle_remove_req)
                future_remove.add_done_callback(self.callback_remove)
            self.path_publish_1.publish(send_goal)
    
    def callback_remove(self, future):
        response = future.result()
        if(response.success):
            turtle_kill_req = Kill.Request()
            turtle_kill_req.name = self.turtle.name
            future = self.kill_client.call_async(turtle_kill_req)
            future.add_done_callback(self.call_kill)
            self.get_logger().info("Turtle got Removed")

    def call_kill(self, future):
        response = future.result()
        self.get_logger().info("Turtule is killed")

def main():
    rclpy.init()
    turtle_controller = TurtleController()
    rclpy.spin(turtle_controller)
    rclpy.shutdown()