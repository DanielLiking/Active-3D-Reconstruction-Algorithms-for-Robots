#!/usr/bin/env python3
# license removed for brevity
import os
envpath = '/home/wl/anaconda3/envs/image_location/lib/python3.6/site-packages/cv2/qt/plugins/platforms'
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = envpath
import rospy
import numpy as np
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge

def talker():
     pub = rospy.Publisher('/tutorial/image', Image, queue_size=1)
     rospy.init_node('talker', anonymous=True)
     rate = rospy.Rate(30)
     bridge = CvBridge()
     Cap = cv2.VideoCapture(0)
     while not rospy.is_shutdown():
         ret, img = Cap.read()
         # cv2.imshow("talker", img)
         cv2.waitKey(3)
         pub.publish(bridge.cv2_to_imgmsg(img, "bgr8"))
         # pub.publish(img)
         rate.sleep()

if __name__ == '__main__':
     try:
         talker()
     except rospy.ROSInterruptException:
         pass


