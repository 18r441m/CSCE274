#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
import random

def player():
    pub = rospy.Publisher('player', String, queue_size=10)
    rospy.init_node('rps_player')
    rate = rospy.Rate(1) # 10HZ
    actions = ['Rock', 'Paper', 'Scissors']
    while not rospy.is_shutdown():
        pub.publish(random.choice(actions))
        rate.sleep()

if __name__ == '__main__':
    try:
        player()
    except rospy.ROSInterruptException:
        pass
