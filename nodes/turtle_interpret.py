#!/usr/bin/env python3

"""
 The turtle_interpret node translates a custom velocity message into a
 geometry_msgs/Twist that can be used by the turtlesim
SUBSCRIBES:
  TurtleVel
"""

import rospy
from turtle_control.msg import TurtleVel
from turtle_control.srv import VelTranslate
from geometry_msgs.msg import Twist, Vector3
from turtlesim.srv import Spawn, SpawnRequest, Kill
from crazy_turtle.srv import Switch, SwitchResponse
from random import uniform



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


class Turtle_Interpret:

    def __init__(self):
        self.sub = rospy.Subscriber("/turtle1/turtle_vel", TurtleVel, self.turtle_vel_callback)
        self.pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size = 10)
        self.serv = rospy.Service("/turtle1/vel_translate", VelTranslate, self.vel_translate_callback)


    def turtle_vel_callback(self, data):
        """ Callback function for turtle_vel topic
        Subscribes to a topic turtle_vel, listening for TurtleVel messages. 
        The subscriber log the input as a debug level message and publishes
        a corresponding geometry_msgs/Twist on cmd_vel.
        
        Args:
          data from the subscricber
        """

        rospy.logdebug(f"Message: {data}")
        twist = turtle_twist(data.linear, data.angular)
        self.pub.publish(twist)


    def vel_translate_callback (self, twist_msg):
        """ Callback function for vel_translate service
        converts a geometry_msgs/Twist into a TurtleVel message and returns it.
        
        Args:
          twist_msg

        Returns:
            TurtleVel message
        """

        if twist_msg.twist.linear.y != 0 or twist_msg.twist.linear.z != 0 or twist_msg.twist.angular.x != 0 or twist_msg.twist.angular.y != 0:
            return None
        return TurtleVel(linear = twist_msg.twist.linear.x, angular = twist_msg.twist.angular.z)


def main():
    """ The main() function. """
    rospy.init_node('turtle_interpret', log_level=rospy.DEBUG)
    Turtle_Interpret()
    rospy.spin()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass