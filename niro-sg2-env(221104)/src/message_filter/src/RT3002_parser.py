#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import rospy
#from std_msgs.msg import String
from custom_msg.msg import RTK
import cantools
import can


if __name__ == '__main__':

    rospy.init_node('message_filter',anonymous=True)
    pub = rospy.Publisher('time_RT3002', RTK, queue_size=10)
    db = cantools.database.load_file('/home/mi/catkin_ws/rt3kfull.dbc')
    pub_data = RTK()

    #while(True):
    while not rospy.is_shutdown():
        can_bus = can.interface.Bus('slcan0', bustype='socketcan')
        data = can_bus.recv()
        
        #if data.arbitration_id == 1537:  #Log/Lat
        if data.arbitration_id == 1536: #date and time
            print(data)
            #print(data.arbitration_id)
            #print(data.data)
            #print(db.decode_message(data.arbitration_id, data.data))       
            decode_messages = db.decode_message(data.arbitration_id, data.data)
            
            pub_data.header.stamp = rospy.Time.now()
            pub_data.header.frame_id = "rtk_time"
            
            pub_data.year = int(str(decode_messages['TimeCentury'])+str(decode_messages['TimeYear']))
            pub_data.month = decode_messages['TimeMonth']
            pub_data.day = decode_messages['TimeDay']
            pub_data.hour = decode_messages['TimeHour']
            pub_data.minute = decode_messages['TimeMinute']
            pub_data.second = decode_messages['TimeSecond']
            pub_data.hsecond = decode_messages['TimeHSecond']

            #pub_data.data = str(decode_messages['TimeCentury']) + "," +  str(decode_messages['TimeMonth']) \
            #                + "," + str(decode_messages['TimeMonth']) + "," + str(decode_messages['TimeDay']) \
            #                + "," + str(decode_messages['TimeHour']) + "," + str(decode_messages['TimeMinute']) \
            #                + "," + str(decode_messages['TimeSecond']) + "," + str(decode_messages['TimeHSecond'])
           
            pub.publish(pub_data)
            print("-" * 5)
    
    #rospy.spin()










