cmake_minimum_required(VERSION 3.0.2)
project(via_navigation)

## Compile as C++11, supported in ROS Kinetic and newer
# add_compile_options(-std=c++11)

## Find catkin macros and libraries
find_package(catkin REQUIRED COMPONENTS
	robot_localization
  roscpp
  message_generation
  std_msgs
)

add_service_files(
   FILES
   RequestGoalPos.srv
)

generate_messages(
  DEPENDENCIES
  std_msgs
)

###################################
## catkin specific configuration ##
###################################
catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES via_navigation
#   CATKIN_DEPENDS robot_localization std_msgs
#  DEPENDS system_lib
)

###########
## Build ##
###########
include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)

## Add executable file
add_executable(send_navigation_goals
	src/send_navigation_goals.cpp
)
add_dependencies(send_navigation_goals ${catkin_EXPORTED_TARGETS})
target_link_libraries(send_navigation_goals
	${catkin_LIBRARIES}
)

