#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import Float32 
from sensor_msgs.msg import LaserScan 
from scan.srv import LidarDatas, LidarDatasResponse

def handle_lidar_datas(req):
    rospy.loginfo('LidarDatas service is working !')
    global tab_init
    global tab_hand
    return LidarDatasResponse(tab_init,tab_hand)


def scan():
    rospy.init_node('scan_values', anonymous=True)
    global flag
    flag = False
    global tab_init
    tab_init = []
    global tab_hand
    tab_hand = []
    rospy.loginfo ('init OK, launching /scan subscribtion and lidar_datas service')
    rospy.Subscriber('/scan', LaserScan , callback)
    rospy.Service('lidar_datas', LidarDatas, handle_lidar_datas)

    # on def un publisher        
    #pub = rospy.Publisher('/datarecue', LaserScan , queue_size=10)
    rospy.spin()

def callback(data):

    # No hand, table detection
    global  flag
    global tab_init
    global tab_hand

    #Enregistrement le premier tableau de data pour initialiser la distance à la table        
    if flag == False :        
        tab_init = data.ranges[0:29] +data.ranges[329:360] #On récupère les distances entre les angles [-30,+30]
        rospy.loginfo('TABLE SANS MAIN:')            
        rospy.loginfo(tab_init)
        flag = True # Pour initialiser le tableau des datas mesurées quand il y a la main (passe dans le if flag == True à présent)
        rospy.sleep(3.)
        rospy.loginfo('Mets ta main si tu es joueur et passe ta main au dessus du télémètre pour lancer une partie sanglante!')
    
    #Hand detection
    if flag == True :
        tab_hand = data.ranges[:29] + data.ranges[329:360] #On récupère les distances entre les angles [-30,+30]
        rospy.loginfo('TABLE Hand:')            
        rospy.loginfo(tab_hand)

        # Test de détection de main
        for i in range(0,len(tab_hand)):
            if (tab_hand[i]- 0.005) < (tab_init[i] - 0.005):
                if ( i!= 0 and tab_hand[i-1] < (tab_init[i-1] - 0.005)):
                    if (i!=59 and tab_hand[i+1] < (tab_init[i+1] - 0.005)):
                           print('MainDetectee')  #test a echanger normalement              
                        #   rospy.loginfo(i)
                        #   rospy.loginfo(tab_hand[i])
                    #    data_output.append([i,tab_hand[i]])          
    
if __name__== '__main__':
    scan() 
          