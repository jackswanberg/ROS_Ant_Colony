#!/usr/bin/env python3
import sys
import rospy
import moveit_commander
from moveit_msgs.msg import DisplayTrajectory
import geometry_msgs.msg
import pickle

def trajectory_callback(msg: DisplayTrajectory):
    rospy.loginfo(msg)
    
    test_file = "pickled_plan"
    with open(test_file,'wb') as fp:
        pickle.dump(msg,fp)

if __name__=="__main__":
    # moveit_commander.roscpp_initialize(sys.argv)
    # rospy.init_node("trajectory_node")

    # rospy.loginfo("Node initialized")

    # rospy.Subscriber("/my_gen3/move_group/display_planned_path", DisplayTrajectory, trajectory_callback)

    # rospy.spin()


    # robot=moveit_commander.RobotCommander(robot_description='/my_gen3/robot_description')
    # scene=moveit_commander.PlanningSceneInterface(ns='gen3')

    # group_name = "gen3"
    # move_group = moveit_commander.move_group.MoveGroupCommander(name='my_gen3', robot_description=group_name)

    # move_group.execute()
    moveit_commander.roscpp_initialize(sys.argv)
    rospy.init_node("planning_node")

    rospy.loginfo("planning Node initialized")


    # rospy.loginfo(type(plan))
    # rospy.loginfo(type(plan.trajectory))
    # robot=moveit_commander.RobotCommander(robot_description='/my_gen3/robot_description')
    # rospy.loginfo(robot.get_group_names())
    # scene=moveit_commander.PlanningSceneInterface(ns='my_gen3')
    # rospy.loginfo(scene.get_objects())

    group_name = "arm"
    move_group = moveit_commander.MoveGroupCommander(group_name,robot_description='/my_gen3/robot_description',ns='my_gen3')
    home_state = move_group.get_current_state()

    number_trajectories = 5
    for i in range(number_trajectories):
        move_group.set_start_state(home_state)
        r = move_group.get_random_joint_values()
        p = move_group.plan(r)
        trajectory_filename = f"pickled_plan{i}"
        with open(trajectory_filename,'wb') as fp:
            rospy.loginfo(type(p))
            pickle.dump(p,fp)