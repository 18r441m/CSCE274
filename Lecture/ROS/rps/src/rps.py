#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
import random

class RPS:
    def __init__(self):
        rospy.Subscriber('player', String, self.callback)
        self.actions = ['Rock', 'Paper', 'Scissors']
        
        # Publishers
        self.cpu_pub = rospy.Publisher('cpu', String, queue_size=10)
        self.game_pub = rospy.Publisher('game', String, queue_size=10)
        self.game = {'player': 0, 'cpu': 0}

    def callback(self, data):
        player = data.data
        cpu = random.choice(self.actions)
        self.cpu_pub.publish(cpu)
        game = self.play(player, cpu)
        self.game_pub.publish(game)
        self.game_pub.publish(str(self.game))
    
    def play(self, player, cpu):
        if player == cpu:
            self.game['player'] += 1
            return str('player: ' + player + ' - cpu: ' + cpu + ' = Result: tie!')
        elif player == 'Rock':
            if cpu == 'Scissors':
                self.game['player'] += 1
                return str('player: ' + player + ' - cpu: ' + cpu + ' = Result: Rock smashes Scissors! Player Won!')
            else:
                self.game['cpu'] += 1
                return str('player: ' + player + ' - cpu: ' + cpu + ' = Result: Paper covers Rock! CPU Won!')
        elif player == 'Paper':
            if cpu == 'Rock':
                self.game['player'] += 1
                return str('player: ' + player + ' - cpu: ' + cpu + ' = Result: Paper covers Rock! Player Won!')
            else:
                self.game['cpu'] += 1
                return str('player: ' + player + ' - cpu: ' + cpu + ' = Result: Scissors cuts Paper! CPU Won!')
        elif player == 'Scissors':
            if cpu == 'Paper':
                self.game['player'] += 1
                return str('player: ' + player + ' - cpu: ' + cpu + ' = Result: Scissors cuts Paper! Player Won!')
            else:
                self.game['cpu'] += 1
                return str('player: ' + player + ' - cpu: ' + cpu + ' = Result: Rock smashes Scissors! CPU Won!')

if __name__ == '__main__':
    try:
        rospy.init_node('RPS')
        RPS()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass

