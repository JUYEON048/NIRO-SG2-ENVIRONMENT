#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import rospy
import message_filters
from sensor_msgs.msg import Image, PointCloud2
#from std_msgs.msg import String
from custom_msg.msg import RTK


def m_filters_callback(img_eth, pcl_left, pcl_right, rtk_timeStamp):
    print("mfilters_callback ::", img_eth.header.stamp.nsecs)


if __name__ == '__main__':

    rospy.init_node('message_filter',anonymous=True)
    
    img_sub_1 = message_filters.Subscriber("/camera/image_color", Image)            #ethernet-camera
    img_sub_2 = message_filters.Subscriber("/camera_array/cam0/image_raw", Image)   #usb-camera

    pcl_sub_1 = message_filters.Subscriber("/Front_velo/velodyne_points", PointCloud2)
    pcl_sub_2 = message_filters.Subscriber("/Left_velo/velodyne_points", PointCloud2)
    pcl_sub_3 = message_filters.Subscriber("/Right_velo/velodyne_points", PointCloud2)

    rtk_sub_1 = message_filters.Subscriber("/time_RT3002", RTK)


    #m_filters = message_filters.ApproximateTimeSynchronizer([img_sub_1, img_sub_2, pcl_sub_1, pcl_sub_2, pcl_sub_3], 10 , 0.1, allow_headerless=False)
    #m_filters = message_filters.ApproximateTimeSynchronizer([img_sub_1, pcl_sub_2, pcl_sub_3, rtk_sub_1], 10 , 1, allow_headerless=True)
    
    m_filters = message_filters.ApproximateTimeSynchronizer([img_sub_1, pcl_sub_2, pcl_sub_3, rtk_sub_1], 10 , 0.1, allow_headerless=False)
    m_filters.registerCallback(m_filters_callback)
    rospy.spin()










