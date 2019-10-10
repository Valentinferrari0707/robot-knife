#ifndef _ROS_SERVICE_LidarDatas_h
#define _ROS_SERVICE_LidarDatas_h
#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"

namespace scan
{

static const char LIDARDATAS[] = "scan/LidarDatas";

  class LidarDatasRequest : public ros::Msg
  {
    public:
      const char* scanDataRequest;

    LidarDatasRequest():
      scanDataRequest("")
    {
    }

    virtual int serialize(unsigned char *outbuffer) const
    {
      int offset = 0;
      uint32_t length_scanDataRequest = strlen(this->scanDataRequest);
      memcpy(outbuffer + offset, &length_scanDataRequest, sizeof(uint32_t));
      offset += 4;
      memcpy(outbuffer + offset, this->scanDataRequest, length_scanDataRequest);
      offset += length_scanDataRequest;
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer)
    {
      int offset = 0;
      uint32_t length_scanDataRequest;
      memcpy(&length_scanDataRequest, (inbuffer + offset), sizeof(uint32_t));
      offset += 4;
      for(unsigned int k= offset; k< offset+length_scanDataRequest; ++k){
          inbuffer[k-1]=inbuffer[k];
      }
      inbuffer[offset+length_scanDataRequest-1]=0;
      this->scanDataRequest = (char *)(inbuffer + offset-1);
      offset += length_scanDataRequest;
     return offset;
    }

    const char * getType(){ return LIDARDATAS; };
    const char * getMD5(){ return "0e7a70afeed50b1374f71a7507da6c78"; };

  };

  class LidarDatasResponse : public ros::Msg
  {
    public:
      uint8_t scanDataResponse_length;
      float st_scanDataResponse;
      float * scanDataResponse;
      uint8_t scanDataHand_length;
      float st_scanDataHand;
      float * scanDataHand;

    LidarDatasResponse():
      scanDataResponse_length(0), scanDataResponse(NULL),
      scanDataHand_length(0), scanDataHand(NULL)
    {
    }

    virtual int serialize(unsigned char *outbuffer) const
    {
      int offset = 0;
      *(outbuffer + offset++) = scanDataResponse_length;
      *(outbuffer + offset++) = 0;
      *(outbuffer + offset++) = 0;
      *(outbuffer + offset++) = 0;
      for( uint8_t i = 0; i < scanDataResponse_length; i++){
      offset += serializeAvrFloat64(outbuffer + offset, this->scanDataResponse[i]);
      }
      *(outbuffer + offset++) = scanDataHand_length;
      *(outbuffer + offset++) = 0;
      *(outbuffer + offset++) = 0;
      *(outbuffer + offset++) = 0;
      for( uint8_t i = 0; i < scanDataHand_length; i++){
      offset += serializeAvrFloat64(outbuffer + offset, this->scanDataHand[i]);
      }
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer)
    {
      int offset = 0;
      uint8_t scanDataResponse_lengthT = *(inbuffer + offset++);
      if(scanDataResponse_lengthT > scanDataResponse_length)
        this->scanDataResponse = (float*)realloc(this->scanDataResponse, scanDataResponse_lengthT * sizeof(float));
      offset += 3;
      scanDataResponse_length = scanDataResponse_lengthT;
      for( uint8_t i = 0; i < scanDataResponse_length; i++){
      offset += deserializeAvrFloat64(inbuffer + offset, &(this->st_scanDataResponse));
        memcpy( &(this->scanDataResponse[i]), &(this->st_scanDataResponse), sizeof(float));
      }
      uint8_t scanDataHand_lengthT = *(inbuffer + offset++);
      if(scanDataHand_lengthT > scanDataHand_length)
        this->scanDataHand = (float*)realloc(this->scanDataHand, scanDataHand_lengthT * sizeof(float));
      offset += 3;
      scanDataHand_length = scanDataHand_lengthT;
      for( uint8_t i = 0; i < scanDataHand_length; i++){
      offset += deserializeAvrFloat64(inbuffer + offset, &(this->st_scanDataHand));
        memcpy( &(this->scanDataHand[i]), &(this->st_scanDataHand), sizeof(float));
      }
     return offset;
    }

    const char * getType(){ return LIDARDATAS; };
    const char * getMD5(){ return "c81553d1e358520792d34f1257625666"; };

  };

  class LidarDatas {
    public:
    typedef LidarDatasRequest Request;
    typedef LidarDatasResponse Response;
  };

}
#endif
