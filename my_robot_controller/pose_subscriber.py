#!/usr/bin/env python3
import rclpy #python library for ros2
from rclpy.node import Node
from turtlesim.msg import Pose

class PoseSubscriberNode(Node):
    def __init__(self):
        super().__init__("pose_subscriber") #Node name as displayed in rqt graph
        self.pose_subscriber = self.create_subscription(Pose, "/turtle1/pose", self.pose_callback, 10) #(msg type, topic, callback function (for subscribers), queue size)

    def pose_callback(self, msg: Pose):
        self.get_logger().info(str(msg))





def main(args=None):
    rclpy.init(args=args)
    node = PoseSubscriberNode()
    rclpy.spin(node) #To keep the node running until you kill it
    
    
    rclpy.shutdown() #To shutdown the node when you kill it
