cmake_minimum_required(VERSION 3.0.2)
project(turtle_control)


## Find catkin macros and libraries
find_package(catkin REQUIRED COMPONENTS
    geometry_msgs
    message_generation
    message_runtime
    turtlesim
)

################################################
## Declare ROS messages, services and actions ##
################################################

## Generate messages in the 'msg' folder
add_message_files(
    FILES
    TurtleVel.msg
 )

## Generate services in the 'srv' folder
add_service_files(
    FILES
    VelTranslate.srv
)

## Generate added messages and services with any dependencies listed here
generate_messages(
    DEPENDENCIES
    turtlesim
)

###################################
## catkin specific configuration ##
###################################
## The catkin_package macro generates cmake config files for your package
## Declare things to be passed to dependent projects
catkin_package(
    CATKIN_DEPENDS
    geometry_msgs
    message_runtime
    turtlesim
)

#############
## Install ##
#############

## Mark executable scripts (Python etc.) for installation
## in contrast to setup.py, you can choose the destination
catkin_install_python(PROGRAMS
    nodes/mover.py
    nodes/talker.py
    nodes/turtle_interpret.py
    nodes/waypoint.py
    DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)