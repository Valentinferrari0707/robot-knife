#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String
from std_msgs.msg import Float64
from scan.srv import LidarDatas

# def demo():


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


def move_motors(angleM1,angleM2,angleM3):
    motor1Pub = rospy.Publisher('/motor1_controller/command', Float64, queue_size=10)
    motor2Pub = rospy.Publisher('/motor2_controller/command', Float64, queue_size=10)
    motor3Pub = rospy.Publisher('/motor3_controller/command', Float64, queue_size=10)
    rospy.sleep(3.)
    print('motor1 publish')
    motor1Pub.publish(angleM1)
    rospy.sleep(1.)
    print('motor2 publish')
    motor2Pub.publish(angleM2)   
    rospy.sleep(1.)
    print('motor3 publish')
    motor3Pub.publish(angleM3)

def processLidarDatas():
    arrayMotorsAngle = [] #[[angleMotor1,angleMotor2,angleMotor3], ...] order => order in the motion sequence 
    return arrayMotorsAngles

def motorsMotion(seqMotorsAngles):
    print(seqMotorsAngles)
    if(len(seqMotorsAngles)!=0):
        for i in range (0,len(seqMotorsAngles)):
            move_motors(seqMotorsAngles[i][0],seqMotorsAngles[i][1],seqMotorsAngles[i][2])
    else:
        print('motion sequence vide !')

def control():

    rospy.init_node('control', anonymous=True)
    # datasLidar = getLidarDatas()
    # seqMotorsAngles = processLidarDatas(datasLidar) #
    # motorsMotion(seqMotorsAngles)
    motorsMotion([[0.5,0.4,-1.2]])
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