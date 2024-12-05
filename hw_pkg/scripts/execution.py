#!/usr/bin/env python3
import sys
import rospy
import moveit_commander
from moveit_msgs.msg import DisplayTrajectory
import geometry_msgs.msg
import pickle

if __name__=="__main__":
    moveit_commander.roscpp_initialize(sys.argv)
    rospy.init_node("execution_node")

    rospy.loginfo("Execution Node initialized")

    group_name = "arm"
    move_group = moveit_commander.MoveGroupCommander(group_name,robot_description='/my_gen3/robot_description',ns='my_gen3')
    home_state = move_group.get_current_joint_values()

    number_trajectories = 5
    for i in range(number_trajectories):
        trajectory_file = f"pickled_plan{i}"
        with open(trajectory_file,'rb') as fp:
            plan = pickle.load(fp)
            rospy.loginfo(plan)
            move_group.execute(plan[1],wait=True)

            move_group.stop()

            # p = move_group.plan(home_state)
            move_group.go(home_state)
            move_group.stop()
            # r = move_group.get_random_joint_values()
            # p = move_group.plan(r)
            # plan = move_group.go(r,wait=True)

            # rospy.loginfo(p[1])
            # rospy.loginfo(home_state)
            # rospy.loginfo(r)
            # rospy.loginfo(p)

            # pose_goal = geometry_msgs.msg.Pose()
            # pose_goal.orientation.w =1
            # pose_goal.orientation.x=0.6
            # pose_goal.orientation.y=0.2
            # pose_goal.orientation.z=0.7
            # move_group.go(r,wait=True)

            # success = move_group.go(wait=True)

