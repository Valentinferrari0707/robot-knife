"""
Created on Thu Oct 10 10:58:50 2019
@author: clara.bouvard, florent.cadot, valentin.ferrari
"""
 
# HOW TO BUILD OUR PROJECT

    1) Clone this project
    2) Go to catkin's workspace "cd catkin_ws"
    3) Build the code with "catkin_make" *
    4) From the catkin_ws folder, source the workspace with the command 
   
    source devel/setup.bash

    *Troubles with "dynamixel_motor" or "rplidar_ros" packages? Delete the two folders in catkin_ws/src and clone them from GitHub : 
   
    git clone https://github.com/Slamtec/rplidar_ros
   
    git clone https://github.com/arebgun/dynamixel_motor

# HOW TO RUN OUR PROJECT
    
    Follow "HOW TO BUILD OUR PROJECT"
    Connect Dynamixels motors and RPlidar

    1- Dynamixel Motors
       
        roslaunch my_dynamixel_tutorial controller_manager.launch
        It should recognize each motors, if it doesn't work check PORT ( default PORT: "/dev/ttyACM0")
        In another terminal : 
       
        roslaunch my_dynamixel_tutorial start_meta_controller.launch        
        If problems: Check Motors Ids in tilt.yaml 

        Test Motor 1: 
        rostopic pub -1 /motor1_controller/command std_msgs/Float64 -- 1.5

        Test Motor 2: 
        rostopic pub -1 /motor2_controller/command std_msgs/Float64 -- 1.5

        Test Motor 3: 
        rostopic pub -1 /motor3_controller/command std_msgs/Float64 -- 1.5
        It still doesn't move ? Check if each motor config is set in Joint Mode.  
        
    2- rplidar_ros and scan
       
        roslaunch rplidar_ros rplidar.launch
           
        roslaunch scan scan.launch 
    

    5- Full Project
        Starting the telemeter measure node:
        In one terminal : 
       
        roscore
       
        In another: 
       
        rosrun rosserial_arduino serial_node.py _port:=/dev/ttyUSB0
    
        ** Be careful to the port! 

        Starting the game: 
       
        roslaunch control control.launch
        In fact, control.launch will launch:
            - rp_lidar.launch
            - dynamixel_motor.launch
            - start_meta_controller.launch 
            - scan.launch
            - The node "control" 

# OUR PROJECT

Our project is about a prototype of the knife game. 
We used a RpLidar, three dynamixel Motors AX-12, a proximity sensor sharp connected to an Arduino and the Robot Operation System (ROS).
At this step of development, this project is not totally successful:
With this code you can start a game passing your hand in front of the telemeter sharp. 
Motors positions are hardcoded because we didn't have time to finish the lidar datas processing function (" processLidarDatas ", see control.py)
However our hand detection is working. 

## License
[MIT](https://choosealicense.com/licenses/mit/)
