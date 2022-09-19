# SUBSCRIBER no topico que mostra posição
# /turtle1/pose

# PUBLISHER no topico que faz a tartaruga se mexer (cmd_vel)
# /turtle1/cmd_vel


#!/usr/bin/env python
import rospy
from geometry_msgs.msg import PoseStamped
from time import sleep

global x , y 

def wait_goal(x_goal,y_goal):
    global x , y 

    #x = x_goal + ou - 0.2 and y = y_goal + ou - 0.2
    #abs(x_goal-x) > 0.2 or abs(y_goal-y) > 0.2
    if ((abs(x_goal-x) > 0.2) or (abs(y_goal-y) > 0.2)):
        wait_goal(x_goal,y_goal)
    else:
        return

if __name__ == '__main__':
    try:

        # Init Node
        rospy.init_node('via_coordinates', anonymous=True)

        # Goal Topic Publisher
        goal_topic = '/move_base_simple/goal'
        coordinates_pub = rospy.Publisher(goal_topic, PoseStamped, queue_size=10)


        #EX DE COORDENADA:'{header: {stamp: now, frame_id: "map"}, pose: {position: {x: 8.0, y: 0.0, z: 0.0}, orientation: {w: 1.0}}}'
        goal_message = PoseStamped()
        goal_message.header.stamp = 'now';
        goal_message.header.frame_id = "map";
        # goal_message.pose.position.x =
        # goal_message.pose.position.y =
        goal_message.pose.position.z = 0;
        goal_message.pose.orientation.w = 1;

       


        while True:
            # LOOP DE COORDENADAS (Inicia se encaminhando ao centro)
            goal_message.pose.position.x = 0;
            goal_message.pose.position.y = 0;
            coordinates_pub.publish(goal_message)
            wait_goal(0,0)
            # INSERIR COORDENADAS DO MAPA
            goal_message.pose.position.x = 8;
            goal_message.pose.position.y = 2;
            coordinates_pub.publish(goal_message)
            wait_goal(8,2)
            goal_message.pose.position.x = -8;
            goal_message.pose.position.y = 4.5;
            coordinates_pub.publish(goal_message)
            wait_goal(-8,4.5)


    except rospy.ROSInterruptException:
        pass
