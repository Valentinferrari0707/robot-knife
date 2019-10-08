#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String
from std_msgs.msg import Float64

def publisher(pub):
    # rospy.loginfo(  .get_caller_id() + 'I heard %s', data.data)
    rospy.sleep(2.)    
    pub.publish(1.5)

def control():

    rospy.init_node('control', anonymous=True)
    pubControl = rospy.Publisher('/joint1_controller/command', Float64, queue_size=10)
    rate = rospy.Rate(10) # 10hz

    publisher(pubControl)
    # while not rospy.is_shutdown():
    #     pubControl.publish(1.5)
    #     rate.sleep()

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    try:
        control()
    except rospy.ROSInterruptException:
        pass