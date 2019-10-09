# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "scan: 0 messages, 1 services")

set(MSG_I_FLAGS "-Istd_msgs:/opt/ros/indigo/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(genlisp REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(scan_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/fs03/share/users/florent.cadot/home/Bureau/Proto/catkin_ws/src/scan/srv/LidarDatas.srv" NAME_WE)
add_custom_target(_scan_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "scan" "/fs03/share/users/florent.cadot/home/Bureau/Proto/catkin_ws/src/scan/srv/LidarDatas.srv" ""
)

#
#  langs = gencpp;genlisp;genpy
#

### Section generating for lang: gencpp
### Generating Messages

### Generating Services
_generate_srv_cpp(scan
  "/fs03/share/users/florent.cadot/home/Bureau/Proto/catkin_ws/src/scan/srv/LidarDatas.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/scan
)

### Generating Module File
_generate_module_cpp(scan
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/scan
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(scan_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(scan_generate_messages scan_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/fs03/share/users/florent.cadot/home/Bureau/Proto/catkin_ws/src/scan/srv/LidarDatas.srv" NAME_WE)
add_dependencies(scan_generate_messages_cpp _scan_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(scan_gencpp)
add_dependencies(scan_gencpp scan_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS scan_generate_messages_cpp)

### Section generating for lang: genlisp
### Generating Messages

### Generating Services
_generate_srv_lisp(scan
  "/fs03/share/users/florent.cadot/home/Bureau/Proto/catkin_ws/src/scan/srv/LidarDatas.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/scan
)

### Generating Module File
_generate_module_lisp(scan
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/scan
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(scan_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(scan_generate_messages scan_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/fs03/share/users/florent.cadot/home/Bureau/Proto/catkin_ws/src/scan/srv/LidarDatas.srv" NAME_WE)
add_dependencies(scan_generate_messages_lisp _scan_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(scan_genlisp)
add_dependencies(scan_genlisp scan_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS scan_generate_messages_lisp)

### Section generating for lang: genpy
### Generating Messages

### Generating Services
_generate_srv_py(scan
  "/fs03/share/users/florent.cadot/home/Bureau/Proto/catkin_ws/src/scan/srv/LidarDatas.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/scan
)

### Generating Module File
_generate_module_py(scan
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/scan
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(scan_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(scan_generate_messages scan_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/fs03/share/users/florent.cadot/home/Bureau/Proto/catkin_ws/src/scan/srv/LidarDatas.srv" NAME_WE)
add_dependencies(scan_generate_messages_py _scan_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(scan_genpy)
add_dependencies(scan_genpy scan_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS scan_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/scan)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/scan
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(scan_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/scan)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/scan
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(scan_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/scan)
  install(CODE "execute_process(COMMAND \"/usr/bin/python\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/scan\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/scan
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(scan_generate_messages_py std_msgs_generate_messages_py)
endif()
