#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import CameraInfo, Image
from cv_bridge import CvBridge
import cv2
import numpy as np

def image_callback(msg: Image):
    #Get +/- 30 degrees infront of turtlebot
    rospy.loginfo(msg.encoding)
    rospy.loginfo(f"(h,w): ({msg.height},{msg.width})")
    cv_image = bridge.imgmsg_to_cv2(msg)
    rospy.loginfo(f"cv_image height and width: ({cv_image.shape})")
    cv2.imshow("Feed",cv_image)
    cv2.waitKey(5)

if __name__=='__main__':
    bridge = CvBridge()
    rospy.init_node("camera_viewer")
    rospy.loginfo("Camera viewer node started")
    # pub = rospy.Publisher("/cmd_vel",Twist,queue_size=10)
    sub = rospy.Subscriber("/camera/rgb/image_raw", Image, callback=image_callback)

    rospy.spin()