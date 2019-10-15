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
    # Gere toute la config de ROS (initialisation du node)
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
    #Donne la distance min
    #Params:
    #data (data.range_min): information sur la dist min
    #on récupère les distances entre les angles [-30,+30]
    #enregistrer le premier tableau de data pour initialiser la distance à la table        

    # No hand, table detection
    global  flag
    global tab_init
    global tab_hand
    if flag == False :        
        tab_init = data.ranges[0:29] +data.ranges[329:360] 
        # rospy.loginfo('TABLE:')            
        # rospy.loginfo(tab_init)
        # # rospy.loginfo('taille table:')
        # # rospy.loginfo(len(tab_init))
        # rospy.loginfo('distance à la table initialisée!')
        # print 'wesh la premiere valeur'
        # print tab_init[29]
        flag = True
        rospy.sleep(3.)
        rospy.loginfo('Mets ta main si tu es joueur et passe ta main au dessus du télémètre pour lancer une partie sanglante!')
    
    #Hand detection
    if flag == True :
        tab_hand = data.ranges[:29] + data.ranges[329:360]
        # rospy.loginfo('TABLE Hand:')            
        # rospy.loginfo(tab_hand)
        # rospy.loginfo('taille table avec main:')
        # rospy.loginfo(len(tab_hand))
        # rospy.loginfo('distance à la table avec main initialisée!')
        # for i in range(0,len(tab_hand)):
        #     if (tab_hand[i]- 0.005) < (tab_init[i] - 0.005):
        #         if ( i!= 0 and tab_hand[i-1] < (tab_init[i-1] - 0.005)):
        #             if (i!=59 and tab_hand[i+1] < (tab_init[i+1] - 0.005)):
        #                    print('MainDetectee')  #test a echanger normalement              
        #                 #   rospy.loginfo(i)
        #                 #   rospy.loginfo(tab_hand[i])
        #             #    data_output.append([i,tab_hand[i]])          
    
    




   
    

        

if __name__== '__main__':
    scan() #on instance scan par c donc c.flag
    #while c.flag == True: #recuperation 1st valeur
    #cd  self.tab_init=c.self.tab_init
    
    
        #pas de la caméra
        #pas= ((data.angle_max)-(data.angle_min))/(data.angle_increment)
        #distmin=min(i for i in data.ranges if str(i) !="nan")
        #self.pub.publish(pas) envoyer info dans pipe
        #rospy.loginfo("I see dist_min %s", pas)
        #rospy.loginfo(self.tab_doigt)
        

## To do : 
# - créer un service qui demande la matrice des distances ( table seule, au démarrage du robot)
# - créer un autre service qui demande la matrice des distances 