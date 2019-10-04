# -*- coding: utf-8 -*-
#!/usr/bin/env python

"""
Created on Fri Oct  4 11:39:54 2019

@author: clara.bouvard

Listener pour récupérer les informations de la RpLidar
"""

import rospy
from std_msgs.msg import Float32
from sensor_msgs.msg import LaserScan

class Scan:
    """ Gere le scan Laser
    """
    global flag
    
    def __init__(self):
        self.configuration_ros()
        """ Gere toute la config de ROS
        """
        self.flag= False

    def configuration_ros(self):
        """ Gere toute la config de ROS
        """

        rospy.init_node('listener', anonymous=True)
        rospy.Subscriber('/scan', LaserScan , self.callback)
        #self.pub = rospy.Publisher('/scan', LaserScan, queue_size=1)
        self.pub = rospy.Publisher('/min_dist', Float32, queue_size=1)

        
    def callback(self,data):
        """Donne la distance min
        Params:
            data (data.range_min): information sur la dist min
        """
        if self.flag== False:
            tab_table=tab_table= data.ranges
            self.flag==True

        #enregistrer le premier tableau de data
        #tab_table= data.ranges
        
        #pas de la caméra
        #pas= ((data.angle_max)-(data.angle_min))/(data.angle_increment)
        #distmin=min(i for i in data.ranges if str(i) !="nan")
        #self.pub.publish(pas) envoyer info dans pipe
        #rospy.loginfo("I see dist_min %s", pas)
        #rospy.loginfo(tab_table)
        rospy.loginfo(tab_table)

if __name__ == '__main__':
    c=Scan()
    rospy.spin()


