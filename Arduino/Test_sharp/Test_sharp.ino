
#include <ros.h>
#include <ros/time.h>
#include <sensor_msgs/Range.h>
#include <std_msgs/Bool.h>
ros::NodeHandle  nh;


sensor_msgs::Range range_msg;
std_msgs::Bool data;


ros::Publisher pub_range( "/range_data", &range_msg);
ros::Publisher pub_distance("/range_distance", &data);




const int analog_pin = 0;
unsigned long range_timer;


/*
 * getRange() - samples the analog input from the ranger
 * and converts it into meters.  
 */
float getRange(int pin_num){
    // Get data
    float sample = (float)analogRead(pin_num)*(5.0F/1024.0F);
    // if the ADC reading is too low, 
    //   then we are really far away from anything
    //if(sample <10)
       // return 254;     // max range
    // Magic numbers to get cm
    //sample= 1309/(sample-3);
    //sample= exp((sample-2.6943363861)/(-0.885130648));
    float distance = 5.0F/sample;

    if (distance > 15) 
      distance= 15;
     return (distance); //convert to meters
}

int getRange_check(int pin_num){
    // Get data
    float sample = (float)analogRead(pin_num)*(5.0F/1024.0F);
    // if the ADC reading is too low, 
    //   then we are really far away from anything
    //if(sample <10)
       // return 254;     // max range
    // Magic numbers to get cm
    //sample= 1309/(sample-3);
    //sample= exp((sample-2.6943363861)/(-0.885130648));
    float distance = 5.0F/sample;

    if (distance > 15) 
      return (false);

    else
      return true;
     
}

char frameid[] = "/ir_ranger";

void setup()
{
  nh.initNode();
  nh.advertise(pub_range);
  nh.advertise(pub_distance);
  range_msg.radiation_type = sensor_msgs::Range::INFRARED;
  range_msg.header.frame_id =  frameid;
  range_msg.field_of_view = 1;
  range_msg.min_range = 2;
  range_msg.max_range = 15;
  
}

void loop()
{
  // publish the range value every 50 milliseconds
  //   since it takes that long for the sensor to stabilize
  if ( (millis()-range_timer) > 50){
    range_msg.range = getRange(analog_pin);
    range_msg.header.stamp = nh.now();
    pub_range.publish(&range_msg);
    
    range_timer =  millis() + 50;


    data.data=getRange_check(analog_pin);
    pub_distance.publish(&data);
  }
  nh.spinOnce();
}
