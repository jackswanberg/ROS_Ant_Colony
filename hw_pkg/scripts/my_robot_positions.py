#!/usr/bin/env python3
import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist

num_robots = 5
g_robots = []
g_position = [{'x':0,'y':0,'z':0}]*num_robots

# class Robot():
#     def __init__(self,position:tuple,odom_sub, velocity_pub):
#         self.odometry_subscriber = odom_sub
#         self.velocity_publisher = velocity_pub
#         self.position = position
#         self.linear = (0,0,0)
#         self.angular = (0,0,0)

#     def get_position(self):
#         return self.position
    
#     def update_position(self):
# def get_position

def odom_callback1(msg: Odometry):
    g_position[0]=msg.pose.pose.position
    rospy.loginfo(f"g_position :{g_position}")
def odom_callback2(msg: Odometry):
    g_position[1]=msg.pose.pose.position
    rospy.loginfo(f"g_position :{g_position}")
def odom_callback3(msg: Odometry):
    g_position[2]=msg.pose.pose.position
    rospy.loginfo(f"g_position :{g_position}")
def odom_callback4(msg: Odometry):
    g_position[3]=msg.pose.pose.position
    rospy.loginfo(f"g_position :{g_position}")
def odom_callback5(msg: Odometry):
    g_position[4]=msg.pose.pose.position
    rospy.loginfo(f"g_position :{g_position}")

def main():
    rospy.init_node("odometry_node")
    rospy.loginfo("Odometry Node started")
    # pub = rospy.Publisher("/cmd_vel",Twist,queue_size=10)

    # num_robots=5 # Find better way to implement this
    callbacks = [odom_callback1,odom_callback2,odom_callback3,odom_callback4,odom_callback5]
    odom = []
    # velocities = []
    for i in range(1,num_robots+1):
        odom.append(rospy.Subscriber(f"Robot{i}/odom", Odometry, callback=callbacks[i-1]))
        pub = rospy.Publisher(f"Robot{i}/cmd_vel",Twist,queue_size=10)
        # g_robots.append(Robot((0,0,0),odom,pub))

    rospy.spin()

if __name__=='__main__':
    main()