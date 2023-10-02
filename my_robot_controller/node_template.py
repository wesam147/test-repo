#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class NameofNodeClass(Node):
    def __init__(self):
        super().__init__("name_of_node")
        self.get_logger().info("Message to be printed when node starts")


def main(args=None):
    rclpy.init(args=args)
    node = NameofNodeClass()
    rclpy.spin(node)
    rclpy.shutdown()