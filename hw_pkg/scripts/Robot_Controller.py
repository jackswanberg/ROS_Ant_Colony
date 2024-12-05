#!/usr/bin/env python3
import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist

rospy.init_node(f"robot_control_node")
rospy.loginfo(f"robot control node started")


class Velocity():
    def __init__(self,x=0,y=0,z=0):
        self.x = x
        self.y = y
        self.z = z

class Robot_Controller():
    def __init__(self,robotid=1, init_pos = (0,0)):
        self.position=init_pos
        self.linear = Velocity()
        self.angular = Velocity()
        
        # rospy.init_node(f"robot_control_node{robotid}")
        # rospy.loginfo(f"robot control node {robotid} started")
        
        
        self.pub = rospy.Publisher(f"Robot{robotid}/cmd_vel",Twist,queue_size=10)
        sub = rospy.Subscriber(f"Robot{robotid}/odom", Odometry, callback=self.odom_callback)

    def odom_callback(self,msg):
        self.position = msg.pose.pose.position
        rospy.loginfo(f"g_position :{self.linear}")
        cmd = Twist()
        cmd.linear.x = self.linear.x
        cmd.linear.y = self.linear.y
        cmd.linear.z = self.linear.z
        cmd.angular.x = self.angular.x
        cmd.angular.y = self.angular.y
        cmd.angular.z = self.angular.z
        self.pub.publish(cmd)


    def update_velocity(self,linear = Velocity(),angular=Velocity()):
        self.linear = linear
        self.angular = angular

if __name__ == "__main__":
    # rospy.init_node(f"robot_control_node")
    # rospy.loginfo(f"robot control node started")

    robot1 = Robot_Controller(1)
    robot2 = Robot_Controller(2)
    robot3 = Robot_Controller(3)
    robot4 = Robot_Controller(4)
    robot5 = Robot_Controller(5)
    rospy.sleep(2)
    robot1.update_velocity(Velocity(0,0,0))
    robot2.update_velocity(Velocity(),Velocity(0,0,0.2))
    robot3.update_velocity(Velocity(),Velocity(0,0,-0.2))
    rospy.sleep(2)
    robot1.update_velocity(Velocity(),Velocity())
    robot2.update_velocity(Velocity(),Velocity())
    robot3.update_velocity(Velocity(),Velocity())
    robot4.update_velocity(Velocity(),Velocity())
    robot5.update_velocity(Velocity(),Velocity())
    rospy.sleep(1)