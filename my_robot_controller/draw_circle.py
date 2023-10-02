#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist #for the message type used my cmd_vel which is geometry_msgs/msg/Twist

class DrawCircleNode(Node):
    def __init__(self):
        super().__init__("draw_circle")
        self.cmd_vel_pub=self.create_publisher(Twist, "/turtle1/cmd_vel", 10) #(msg type, topic, callback function (for subscribers), queue size)
        self.timer = self.create_timer(0.5, self.send_vel_command)
        self.get_logger().info("Drawing Circle")

    def send_vel_command(self):
        msg = Twist()
        msg.linear.x = 2.0
        msg.angular.z = 1.0
        self.cmd_vel_pub.publish(msg)

def main(args=None):
    rclpy.init(args=args)

    node = DrawCircleNode()
    rclpy.spin(node)

    rclpy.shutdown()