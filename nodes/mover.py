#!/usr/bin/env python
# Copy this file into your homework repository and fill in the <> blanks in the document strings
""" 
Publishes twist that will move a robot back and forth in the x direction 
while randomly providing a <angular> velocity about the Z-axis.

PUBLISHERS:
  + cmd_vel (Twist) ~ the velocity of an erratic turtle path

SERVICES:
  + switch (Switch) ~ position of the new turtle

"""

import rospy
from geometry_msgs.msg import Twist, Vector3
from random import uniform
from crazy_turtle.srv import Switch, SwitchResponse
from turtlesim.srv import Spawn, SpawnRequest
from turtlesim.srv import Kill

def turtle_twist(xdot, omega):
    """ Create a twist suitable for a turtle

        Args:
           xdot (float) : the forward velocity
           omega (float) : the angular velocity

        Returns:
           Twist - a 2D twist object corresponding to linear/angular velocity
    """
    return Twist(linear = Vector3(x = xdot, y = 0, z = 0),
                  angular = Vector3(x = 0, y = 0, z = omega))

class Mover:
    """ Publishes movement geometry_msgs/Twist commands at a fixed rate 
    """
    def __init__(self):
        self.nsteps = 0
        self.direction = 1
        self.velocity = rospy.get_param("~velocity")
        self.pub = rospy.Publisher('cmd_vel', Twist, queue_size = 10)
        self.switch = rospy.Service("switch", Switch, self.switch_callback)
        self.kill = rospy.ServiceProxy("kill", Kill)
        self.spawn = rospy.ServiceProxy("spawn", Spawn)
        self.tmr = rospy.Timer(rospy.Duration(0.01), self.timer_callback)


    def switch_callback(self, pose):
        """ Callback function for the switch service
        
        Kills turtle1 and respawns it an a new location

         Args:
          pose (SwitchRequest): the mixed_up field contains
             x, y, linear and angular velocity components
             that are used to determine the new turtle location

        Returns:
           A SwitchResponse, containing the new x and y position
        """
        self.kill("turtle1")
        # The new position of the turtle is intentionally scrambled from a weird message
        newx = pose.mixed_up.x * pose.mixed_up.angular_velocity
        newy = pose.mixed_up.y * pose.mixed_up.linear_velocity
        self.spawn(x = newx, y = newy, theta = pose.mixed_up.theta, name = "turtle1")
        return SwitchResponse(x = newx, y = newy)

    def timer_callback(self, event):
        """ Handle the timer callback.

        Args:
          event (TimerEvent): This timer doesn't use any of the event info.
        """
        twist = turtle_twist(self.direction * self.velocity, uniform(-20, 20))

        self.nsteps += 1
        if self.nsteps > 200:
            self.nsteps = 0
            self.direction *= -1

        self.pub.publish(twist)

def main():
    """ The main() function. """
    rospy.init_node('mover')
    mymove = Mover()
    rospy.spin()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
