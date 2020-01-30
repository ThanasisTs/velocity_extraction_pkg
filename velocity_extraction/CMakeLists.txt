cmake_minimum_required(VERSION 2.8.3)
project(velocity_extraction)

find_package(catkin REQUIRED COMPONENTS
  geometry_msgs
  roscpp
  rospy
  velocity_extraction_msg
  message_generation
)

## Generate services in the 'srv' folder


catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES velocity_extraction
 CATKIN_DEPENDS geometry_msgs roscpp rospy message_runtime
#  DEPENDS system_lib
)

include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)

