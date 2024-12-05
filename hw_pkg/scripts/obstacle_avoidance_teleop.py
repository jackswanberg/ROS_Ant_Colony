#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

def laserscan_callback(msg: LaserScan):
    #Get +/- 30 degrees infront of turtlebot
    # global g_set_velocity
    # global blocked
    ranges = msg.ranges
    closest = min([min(ranges[:40]),min(ranges[-40:])])
    cmd = Twist()
    # rospy.loginfo(f"{closest}")
    if closest<0.35:
        blocked = 1
        g_set_velocity = 1
        cmd.linear.x = 0.0
        cmd.angular.z = -0.5
        pub.publish(cmd)
    # else:
    #     blocked = 0
        
    # if not blocked and g_set_velocity:
    #     g_set_velocity = 0
    #     cmd.linear.x = 0.3
    #     cmd.angular.z = 0.0
    #     pub.publish(cmd)

if __name__=='__main__':
    rospy.init_node("turtlebot_obstacle_avoidance")
    g_set_velocity = 0
    blocked = 0
    pub = rospy.Publisher("/cmd_vel",Twist,queue_size=10)
    sub = rospy.Subscriber("/scan", LaserScan, callback=laserscan_callback)

    rospy.spin()