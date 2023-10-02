#!/usr/bin/env python3
import rclpy #python library for ros2
from rclpy.node import Node

class MyNode(Node):
    def __init__(self):
        super().__init__("first_node") #Node name as displayed in rqt graphy
        self.counter_ = 0
        self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        self.get_logger().info("Hello "+ str(self.counter_))
        self.counter_ += 1





def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node) #To keep the node running until you kill it
    
    
    rclpy.shutdown() #To shutdown the node when you kill it

if __name__ == '__main__':
    main()