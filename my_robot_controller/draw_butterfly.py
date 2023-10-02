#!/usr/bin/env python3
import rclpy
import numpy as np
import math
import sympy as sp
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose


class Drawing(Node):
    h = 0
    def __init__(self):
        super().__init__("drawing")
        self.get_logger().info("Drawing started")
        self.cmd_vel_pub = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)
        timer_period = 0.0001
        #self.pose_subscriber = self.create_subscription(Pose, "/turtle1/pose", self.pose_callback, 10) #(msg type, topic, callback function (for subscribers), queue size)
        h = 0
        self.timer = self.create_timer(timer_period, self.drawing)

    def drawing(self):
        #t = self.get_clock().now().to_msg().sec
        #for t in range (100):
        t = self.h
        u = math.sin(t/12)
        z = math.cos(t)
        e = 2.71
        x = math.sin(t)*(8*math.sin(4*t)-math.pow(e,z) * math.sin(t) - ((5*math.cos(t/12)*math.pow(u,4))/(12)) ) + math.cos(t)*(-2*math.cos(4*t) + math.pow(e,z)-math.pow(u,5))
        y = math.cos(t)*(8*math.sin(4*t)-math.pow(e,z) * math.sin(t) - ((5*math.cos(t/12)*math.pow(u,4))/(12)) ) - math.sin(t)*(-2*math.cos(4*t) + math.pow(e,z)-math.pow(u,5))
        #x = math.sin(t) * (math.exp(math.cos(t)) - 2 * math.cos(4 * t) - math.pow(math.sin(t/12), 5))
        #y = math.cos(t) * (math.exp(math.cos(t)) - 2 * math.cos(4 * t) - math.pow(math.sin(t/12), 5))
            
        #x = -1*math.sin(self.h)
        #y = math.cos(self.h)
        self.h = self.h+0.0001
        # Symbolic variables
        #t_sym = sp.Symbol('t')
        #x_sym = sp.sin(t_sym) * (sp.exp(sp.cos(t_sym)) - 2 * sp.cos(4 * t_sym) - sp.sin(t_sym/12)**5)
        #y_sym = sp.cos(t_sym) * (sp.exp(sp.cos(t_sym)) - 2 * sp.cos(4 * t_sym) - sp.sin(t_sym/12)**5)

        # Differentiate to obtain velocities
        #v_x_sym = sp.diff(x_sym, t_sym)
        #v_y_sym = sp.diff(y_sym, t_sym)

        # Substitute the current time 't' for velocities
        #v_x = v_x_sym.subs(t_sym, t)
        #v_y = v_y_sym.subs(t_sym, t)

        cmd = Twist()
        #cmd.linear.x= float(v_x)
        #cmd.linear.y= float(v_y)
        cmd.linear.x= x
        cmd.linear.y= y
        self.cmd_vel_pub.publish(cmd)


def main(args=None):
    rclpy.init(args=args)
    node = Drawing()
    rclpy.spin(node)
    rclpy.shutdown()