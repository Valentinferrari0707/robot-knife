#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String
from std_msgs.msg import Float64
from std_msgs.msg import Bool
from scan.srv import LidarDatas

#Dans le cas où le lidar ne marcherait pas 
def demo():
    seqMotion =[[0,0.4,-0.9],[1.3,1,-1],[1.3,0.2,-1],[1.5,0.2,-1],[1.7,0.2,-1],[1.9,0.2,-1],[2.1,0.2,-1],[2.4,0.2,-1],[0,0.4,-0.9]]
    motorsMotion(seqMotion)    

#Not working for the moment, Attend que l'utilisateur mette sa main devant le télémètre avant de lancer la mise en route
def handle_start(data): 
    global start_flag
    rospy.loginfo(start_flag)
    rospy.loginfo(data)
    if (data == True) and (start_flag ==False):
        start_flag=True

#Utilise un service pour obtenir les donées du lidar
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

#Bouge chaque moteur grâce à des commandes en angle
def move_motors(angleM1,angleM2,angleM3):
    motor1Pub = rospy.Publisher('/motor1_controller/command', Float64, queue_size=10)
    motor2Pub = rospy.Publisher('/motor2_controller/command', Float64, queue_size=10)
    motor3Pub = rospy.Publisher('/motor3_controller/command', Float64, queue_size=10)
    # rospy.sleep(3.)
    print('motor1 publish')
    motor1Pub.publish(angleM1)
    # rospy.sleep(1.)
    print('motor2 publish')
    motor2Pub.publish(angleM2)   
    # rospy.sleep(1.)
    print('motor3 publish')
    motor3Pub.publish(angleM3)
    rospy.sleep(2.)


#A finir ! Traite les donées reçues par le lidar pour générer une séquence de liste d'angles (pour chaque moteur)   
def processLidarDatas():
    arrayMotorsAngle = [] #[[angleMotor1,angleMotor2,angleMotor3], ...] order => order in the motion sequence 
    return arrayMotorsAngles

#Publie dans les topics des moteurs pour les déplacer
def motorsMotion(seqMotorsAngles):
    print(seqMotorsAngles)
    if(len(seqMotorsAngles)!=0):
        for i in range (0,len(seqMotorsAngles)):
            move_motors(seqMotorsAngles[i][0],seqMotorsAngles[i][1],seqMotorsAngles[i][2])
            # rospy.sleep(1.)
    else:
        print('motion sequence vide !')


def control():

    rospy.init_node('control', anonymous=True)
    # datasLidar = getLidarDatas()
    # seqMotorsAngles = processLidarDatas(datasLidar) #
    # motorsMotion(seqMotorsAngles)
    global start_flag
    start_flag=False
    # rospy.Subscriber("/range_distance", Bool, handle_start, queue_size=10)
    demo()  
    # if start_flag == True:
    #     motorsMotion([[0,0.4,-0.9]])

    # motorsMotion([[0.5,0.4,-0.9]])
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