# MECH_ENG_495 - Homework 1
GitHub repository - https://github.com/YaelBenShalom/Turtle-Control

## Overview
This package lets the simulated turtle follow a series of waypoints. The package depends on turtlesim - it's designed to control the turtle and uses messages/services from the turtlesim package.
The turtle chase after another turtle (Mark), and when he's close to catch him, Mark transports himself the the next waypoint.


## Usage and Configuration Instructions

1. To start running the turtlebot in figure-eight trajectory, run `roslaunch turtle_control waypoint_follow.launch `.
![turtle_control node](https://github.com/YaelBenShalom/Turtle-Control/blob/master/GIFs/turtle%20race%20-%20HW1.gif)