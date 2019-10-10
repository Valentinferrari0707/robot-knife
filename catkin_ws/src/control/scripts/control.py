#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String
from std_msgs.msg import Float64
from scan.srv import LidarDatas

def getLidarDatas():
    # Get datas when no hand
    # rospy.wait_for_service('lidar_datas')
    # try:
    #     lidar_datas = rospy.ServiceProxy('lidar_datas', LidarDatas)
    #     resp = lidar_datas('chdsb')
    #     rospy.loginfo('reponse du service:')
    #     rospy.loginfo(resp)
    #     return resp.scanDataResponse
    # except rospy.ServiceException, e:
    #     print "Service call failed: %s"%e

    # Get datas when hand
    rospy.sleep(3.)
    rospy.loginfo('get datas with hand')
    rospy.wait_for_service('lidar_datas')
    try:
        lidar_datas = rospy.ServiceProxy('lidar_datas', LidarDatas)
        resp = lidar_datas('Give me datas with hand')
        rospy.loginfo('reponse du service:')
        rospy.loginfo(resp)
        return resp.scanDataHand
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e


def publisher(pub):
    # rospy.loginfo(  .get_caller_id() + 'I heard %s', data.data)
    rospy.sleep(2.)    
    pub.publish(1.5)

def control():

    rospy.init_node('control', anonymous=True)
    getLidarDatas()
    rospy.sleep(3.)
    # control = rospy.Publisher('/joint1_controller/command', Float64, queue_size=10)
    # rate = rospy.Rate(10) # 10hz

    # publisher(pubControl)
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