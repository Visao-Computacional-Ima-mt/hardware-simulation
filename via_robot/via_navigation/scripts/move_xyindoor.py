# SUBSCRIBER no topico que mostra posição
# /turtle1/pose

# PUBLISHER no topico que faz a tartaruga se mexer (cmd_vel)
# /turtle1/cmd_vel


#!/usr/bin/env python
import rospy
from geometry_msgs.msg import PoseStamped
from time import sleep
from nav_msgs.msg import Odometry
import math


def Posecallback(pose_message):
    global x
    global y, theta

    # calculation of theta from quaterinion
    quaternion = pose_message.pose.pose.orientation
    x = quaternion.x
    y = quaternion.y
    z = quaternion.z
    w = quaternion.w
    theta = math.atan2(2 * (w * z + x * y), 1 - 2 * (y * y + z * z))

    # position x and y from odometry
    x = pose_message.pose.pose.position.x
    y = pose_message.pose.pose.position.y

def wait_goal(x_goal,y_goal):
    global x , y 

    #x = x_goal + ou - 0.2 and y = y_goal + ou - 0.2
    #abs(x_goal-x) > 0.2 or abs(y_goal-y) > 0.2
    while ((abs(x_goal-x) > 0.2) or (abs(y_goal-y) > 0.2)):
        print("Going")
    
    return

if __name__ == '__main__':
    try:

        # Init Node
        rospy.init_node('via_coordinates', anonymous=True)

        # Goal Topic Publisher
        goal_topic = '/move_base_simple/goal'
        coordinates_pub = rospy.Publisher(goal_topic, PoseStamped, queue_size=10)

        # Init Pose Subscriber
        position_topic = "/odometry/filtered"
        rospy.Subscriber(position_topic, Odometry, Posecallback)
        sleep(2)


        #EX DE COORDENADA:'{header: {stamp: now, frame_id: "map"}, pose: {position: {x: 8.0, y: 0.0, z: 0.0}, orientation: {w: 1.0}}}'
        goal_message = PoseStamped()
        now = rospy.get_rostime()
        goal_message.header.stamp = now;
        goal_message.header.frame_id = "map";
        # goal_message.pose.position.x =
        # goal_message.pose.position.y =
        goal_message.pose.position.z = 0;
        goal_message.pose.orientation.w = 1;

       


        #while True:
        # LOOP DE COORDENADAS (Inicia se encaminhando ao centro)
        # goal_message.pose.position.x = 0;
        # goal_message.pose.position.y = 0;
        # coordinates_pub.publish(goal_message)
        # wait_goal(0,0)
        # INSERIR COORDENADAS DO MAPA
        goal_message.pose.position.x = 2;
        goal_message.pose.position.y = 0;
        coordinates_pub.publish(goal_message)
        # wait_goal(2,0)
        goal_message.pose.position.x = -2;
        goal_message.pose.position.y = 1;
        coordinates_pub.publish(goal_message)
        # wait_goal(-2,1)


    except rospy.ROSInterruptException:
        pass
