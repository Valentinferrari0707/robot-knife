#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import math 
import numpy
from std_msgs.msg import String
from std_msgs.msg import Float64
from std_msgs.msg import Bool
from scan.srv import LidarDatas

#Positions des moteurs envoyées en dur 
def demo():
    seqMotion =[[0,0.4,-0.9],[1.3,1,-1],[1.3,0.2,-1.1],[1.3,0.4,-0.9],[1.5,0.4,-0.9],[1.5,0.2,-1.1],[1.5,0.4,-0.9],[1.7,0.4,-1],[1.7,0.2,-1.1],[1.7,0.4,-0.9],[1.9,0.4,-1],[1.9,0.2,-1.1],[1.9,0.4,-1],[2.1,0.4,-1],[2.1,0.2,-1.1],[2.1,0.4,-1],[0,0.4,-0.9]]
    motorsMotion(seqMotion)    

#Attend que l'utilisateur mette sa main devant le télémètre avant de lancer la mise en route
def handle_start(data): 
    global start_flag
    if (data.data == True) and (start_flag ==False):
        print('Debut programme!')
        start_flag=True
        datasLidar = getLidarDatas()
        seqMotorsAngles = processLidarDatas(datasLidar)
        motorsMotion(seqMotorsAngles)
        # demo()

#Utilise le service 'lidar_data' pour obtenir les donées du lidar
def getLidarDatas():
    rospy.sleep(3.)
    rospy.loginfo('get datas with hand')
    rospy.wait_for_service('lidar_datas')
    try:
        lidar_datas = rospy.ServiceProxy('lidar_datas', LidarDatas)
        resp = lidar_datas('Lidar give me some datas')
        return resp
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

#Bouge chaque moteur grâce à des commandes en angle, en publiant dans leurs topics respectifs
def move_motors(angleM1,angleM2,angleM3):
    motor1Pub = rospy.Publisher('/motor1_controller/command', Float64, queue_size=10)
    motor2Pub = rospy.Publisher('/motor2_controller/command', Float64, queue_size=10)
    motor3Pub = rospy.Publisher('/motor3_controller/command', Float64, queue_size=10)
    print('Publish in motors controller topics!')
    motor1Pub.publish(angleM1)
    motor2Pub.publish(angleM2)   
    motor3Pub.publish(angleM3)
    rospy.sleep(1.)

#Appelle la fonction qui bouge chaque moteur pour chaque valeur d'angle
def motorsMotion(seqMotorsAngles):
    global start_flag
    print(seqMotorsAngles)
    if(len(seqMotorsAngles)!=0):
        for i in range (0,len(seqMotorsAngles)):
            move_motors(seqMotorsAngles[i][0],seqMotorsAngles[i][1],seqMotorsAngles[i][2])
            # rospy.sleep(1.)
    else:
        print('motion sequence vide !')
    start_flag = False #Permet de recommencer une nouvelle partie en approchant sa main du télémètre


#Traite les donées reçues par le lidar pour générer une séquence de liste d'angles pour commander les moteurs
#Ne marche pas
def processLidarDatas(datasLidar):
    tab_init = datasLidar.scanDataResponse
    tab_hand = datasLidar.scanDataHand
    tab_hand_x = [] #liste des positions.
    arrayMotorsAngle = [] #[[angleMotor1,angleMotor2,angleMotor3], ...] order => order in the motion sequence 
    L1 = 0.067  # longueur entre M1 et M2
    L2 = 0.165# longueur entre M3 et l'effecteur
    Y=0.02  #!!!! toujours inf à 0.07 ( hauteur de l'effecteur)

    for i in range(0,len(tab_hand)):
        if (tab_hand[i]- 0.005) < (tab_init[i] - 0.005):
            if ( i!= 0 and tab_hand[i-1] < (tab_init[i-1] - 0.005)):
                if (i!=59 and tab_hand[i+1] < (tab_init[i+1] - 0.005)):
                    if(i<29):
                        tab_hand_x.append([i,tab_hand[i]])
                    else:
                        tab_hand_x.append([i+299,tab_hand[i]]) #correspondance angle 30° avec 329  
   
    for j in range(0,len(tab_hand_x)):
        # print("values in process")
        # print(tab_hand_x[j][0])
        # print(tab_init[tab_hand_x[j][0]])        
        # X= abs(((tab_init[tab_hand_x[j][0]]* math.cos(54)) /(math.cos(tab_hand_x[j][0])))) - 0.2 #54: Angle inclinaison lidar
        # X= math.cos(tab_hand_x[j][0])*tab_hand_x[j][1]
        # print("distance !!!!")
        # print(X)
        X = tab_hand_x[j][1]-0.2
        # print("go dans acos")
        # print(( X**2 + Y**2 - L1**2 - L2**2) / (2*L1*L2))
        # AM3d = math.acos(( X**2 + Y**2 - L1**2 - L2**2) / (2*L1*L2))
        # AM3r = AM3d * math.pi / 180 #angle Moteur 2 en radiant celui envoye au moteur
        AM3r=-0.9
        Yam2=L2 * math.cos(AM3r)*Y - L2 * math.sin(AM3r)*X + L1*Y
        Xam2=L2 * math.cos(AM3r)*Y + L2 * math.cos(AM3r)*X + L1*X
        AM2d = numpy.arctan2(Yam2 ,Xam2)
        AM2r = AM2d * math.pi / 180
        print("variable AM2")
        print(AM2r)
        AM1r = math.acos(0.15/(tab_hand_x[j][1] -0.2))
        # print(AM1r)
        # print("ca passe")
        # arrayMotorsAngle.append([AM1r,AM2r,AM3r])
        # AM1r=tab_hand_x[j][0]* math.pi / 180
        # AM3r=90* math.pi / 180
        print("ca passe")
        print(AM1r)
        # AM3r=tab_hand_x[j][0]* math.pi / 180
        # AM3r=(tab_hand_x[j][0]+90)* math.pi / 180
        arrayMotorsAngle.append([AM1r,AM2r,-0.9])        
        arrayMotorsAngle.append([AM1r,0.4,-0.9])
    # print(arrayMotorsAngle)
    # print(tab_init)
    # print(tab_hand_x)
    arrayMotorsAngle.append([0,0.4,-0.9])
    return arrayMotorsAngle



def control():
    rospy.sleep(4.)
    rospy.init_node('control', anonymous=True)
    global start_flag
    start_flag=False
    rospy.Subscriber("/range_distance", Bool, handle_start, queue_size=10)
    motorsMotion([[0,0.4,-0.9],[0,0.4,-0.9]]) #Set motors à la position initiale  
    rospy.sleep(3.)
    rospy.spin()

if __name__ == '__main__':
    try:
        control()
    except rospy.ROSInterruptException:
        pass