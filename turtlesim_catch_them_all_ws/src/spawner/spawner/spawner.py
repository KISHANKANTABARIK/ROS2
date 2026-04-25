import rclpy
import random
import math
from rclpy.node import Node
from turtlesim.srv import Spawn
from turtle_interface.msg import Turtle, TurtleArray
from turtle_interface.srv import CatchTurtle

class Spawner(Node):
    def __init__(self):
        super().__init__("spawner")
        self.counter = 2
        self.alive_turtle = TurtleArray()
        self.spawn_client = self.create_client(Spawn, "/spawn")
        self.turtle_publisher = self.create_publisher(TurtleArray, "/turtle_array",10)

        self.create_service(CatchTurtle, "/catch_turtle", self.callback_catch_turtle)

        self.create_timer(3.0, self.call_spawner)

    def call_spawner(self):
        while(not self.spawn_client.wait_for_service(1.0)):
            self.get_logger().warn("Server is not running")
        
        turtle = Turtle()

        x = turtle.x = round(random.uniform(1,10),2) 
        y = turtle.y = round(random.uniform(1,10),2)
        theta = turtle.theta = round(random.uniform(-math.pi, math.pi),2)
        name = turtle.name = f"turtle{self.counter}"
        self.alive_turtle.turtle_array.append(turtle)
        self.turtle_publisher.publish(self.alive_turtle)
        self.spawn_turtles(x, y, theta, name)
        self.counter += 1

    def spawn_turtles(self, x, y, theta, name):
        spawn = Spawn.Request()
        spawn.x = x
        spawn.y = y
        spawn.theta = theta
        spawn.name = name

        future = self.spawn_client.call_async(spawn)
        future.add_done_callback(self.callback_response)

    def callback_response(self, future):
        response = future.result()
        if(response.name != ""):
            self.get_logger().info(f"Turtle spwaned: {self.counter}")

    def callback_catch_turtle(self, request: CatchTurtle.Request, response: CatchTurtle.Response):
        for turtle in self.alive_turtle.turtle_array:
            if(turtle.name == request.name):
                self.alive_turtle.turtle_array.remove(turtle)
                response.success = True
                break
            else:
                response.success = False
        return response

def main():
    rclpy.init()
    spawner = Spawner()
    rclpy.spin(spawner)
    rclpy.shutdown()