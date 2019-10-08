#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import Float32
from sensor_msgs.msg import LaserScan

class Scan:
    def __init__(self):
        self.configuration_ros()
        # Gere toute la config de ROS

        self.flag= False
        print "init OK"
        self.tab_table = ''
        print "then ?"

    def configuration_ros(self):
        rospy.init_node('listener', anonymous=True)
        rospy.Subscriber('/scan', LaserScan , self.callback)
        #self.pub = rospy.Publisher('/scan', LaserScan, queue_size=1)
        #self.pub = rospy.Publisher('/min_dist', Float32, queue_size=1)

        
    def callback(self,data):
        #Donne la distance min
        #Params:
        #data (data.range_min): information sur la dist min
        
        if self.flag== False:
            self.tab_table= data.ranges
            rospy.loginfo(self.tab_table)
            rospy.loginfo(len(self.tab_table))
            self.flag=True  
        #enregistrer le premier tableau de data
        #tab_table= data.ranges
        
        #pas de la caméra
        #pas= ((data.angle_max)-(data.angle_min))/(data.angle_increment)
        #distmin=min(i for i in data.ranges if str(i) !="nan")
        #self.pub.publish(pas) envoyer info dans pipe
        #rospy.loginfo("I see dist_min %s", pas)
        #rospy.loginfo(tab_table)
        

if __name__== '__main__':
    c=Scan() #on instance scan par c donc c.flag
    rospy.sleep(1)
    while c.flag == True: #recuperation 1st valeur
        tab_table=c.tab_table
        rospy.sleep(1)
    rospy.spin()


