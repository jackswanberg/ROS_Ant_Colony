#!/usr/bin/env python3
import rospy
import math
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist, PoseStamped
from move_base_msgs.msg import MoveBaseActionGoal

# rospy.init_node(f"robot_control_node")
# rospy.loginfo(f"robot control node started")

if __name__=="__main__":
    rospy.init_node("goal_setter")
    rospy.loginfo("Initialized goal setting node")

    # pub = rospy.Publisher("/move_base/goal",MoveBaseActionGoal,queue_size=10)
    # cmd = MoveBaseActionGoal()
    # cmd.goal.target_pose.pose.position.x=5
    pub = rospy.Publisher("/move_base_simple/goal",PoseStamped,queue_size=10)
    cmd = PoseStamped()
    cmd.pose.position.x = 5
    status = pub.publish(cmd)
    rospy.loginfo(status)
    rospy.spin()