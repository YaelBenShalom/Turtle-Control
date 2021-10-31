# Tutle Control


## Table of Contents

- [Description](#description)
- [Getting Started](#getting-started)
- [Usage and Configuration Instructions](#usage-and-configuration-instructions)


## Description
This package lets the simulated turtle follow a series of waypoints. The package depends on turtlesim - it's designed to control the turtle and uses messages/services from the turtlesim package.<br>
The turtle chases after another turtle (Mark), and when he's close to catch him, Mark transports himself to the next waypoint.


## Getting Started

Create a workspace, clone the repo, and build the workspace:
```
mkdir -p ws/src && cd ws/src
git clone https://github.com/YaelBenShalom/Turtle-Control.git
cd ../..
catkin_make
source devel/setup.bash 
```


## Usage and Configuration Instructions

To start running the turtlebot in figure-eight trajectory, run `roslaunch Turtle-Control waypoint_follow.launch`.

<p align="center">
  <img align="center" src="https://github.com/YaelBenShalom/Turtle-Control/blob/master/GIFs/turtle%20race%20-%20HW1.gif">
</p>
