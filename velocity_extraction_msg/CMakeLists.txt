cmake_minimum_required(VERSION 2.8.3)
project(velocity_extraction_msg)


find_package(catkin REQUIRED COMPONENTS
  geometry_msgs
  std_msgs
  roscpp
  rospy
  trajectory_smoothing_msg
  message_generation
)


add_message_files(
  FILES
  TwistFromPoint.msg
)

add_service_files(
  FILES
  TwistFromPoints.srv
)

## Generate added messages and services with any dependencies listed here
generate_messages(
  DEPENDENCIES
  trajectory_smoothing_msg
  geometry_msgs
  std_msgs
)


catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES velocity_extraction_msg
 CATKIN_DEPENDS geometry_msgs roscpp rospy message_runtime
#  DEPENDS system_lib
)


include_directories(
  include
  ${catkin_INCLUDE_DIRS}
)
