execute_process(COMMAND "/fs03/share/users/florent.cadot/home/catkin_ws/build/dynamixel_motor/dynamixel_controllers/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/fs03/share/users/florent.cadot/home/catkin_ws/build/dynamixel_motor/dynamixel_controllers/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
