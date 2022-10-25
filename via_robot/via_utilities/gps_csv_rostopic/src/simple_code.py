#!/usr/bin/env python3

import numpy as np
import rospy                                                                 
from std_msgs.msg import String               
from sensor_msgs.msg import NavSatFix 
import sys         
import csv
import os

rows = []
path = os.path.dirname(__file__).split("/")
path[-1] = 'csv'
path = '/'.join(path)

args = rospy.myargv(argv=sys.argv)
if len(args) < 3:
    database = 'Teste2.csv'
else:
    database = args[1]

pub = rospy.Publisher('gps/fix', NavSatFix, queue_size=10)
rospy.init_node('GPS_reader_node', anonymous=True)

rospy.loginfo("Initialising...")
# build navsat message
fake_gps = NavSatFix()


with open(path  + "/" + database, 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)

    i=0
    print('Publishing GPS Info \n')

    for row in csvreader:
        if not rospy.is_shutdown():
            #Assuming that parse will return these values
            rospy.sleep(1)
            i = i + 1
            rows.append(row)

            # Header
            fake_gps.header.seq = i
            fake_gps.header.frame_id = 'gps'
            fake_gps.header.stamp = rospy.Time.now()
            print(fake_gps.header)


            # Status Fix
            if row[6] == 'GPS':
                fake_gps.status.status = fake_gps.status.STATUS_FIX
                print('Status = ',fake_gps.status.status,' (Unable to fix position)')
            elif row[6] == 'DGPS':
                fake_gps.status.status = fake_gps.status.STATUS_SBAS_FIX
                print('Status = ',fake_gps.status.status,' (Satellite-based Augmentation - DGPS)')
            elif row[6] == 'fRTK':
                fake_gps.status.status = fake_gps.status.STATUS_GBAS_FIX
                print('Status = ',fake_gps.status.status,' (Ground-based Augmentation - fRTK)')
            else:
                fake_gps.status.status = fake_gps.status.STATUS_NO_FIX
                print('Status = ',fake_gps.status.status,' (Unable to fix position)')
            
            fake_gps.status.service = 1 

            # Coordinates
            fake_gps.latitude = np.float64(row[2])
            fake_gps.longitude = np.float64(row[3])
            fake_gps.altitude = np.float64(row[4])

            print('Latitude = ',fake_gps.latitude)
            print('Longitude = ',fake_gps.longitude)
            print('Altitude = ',fake_gps.altitude)

            #Extra Info
            print('PDOP = ',row[7])
            print('HDOP = ',row[8])
            print('VDOP = ',row[9],'\n')


            pub.publish(fake_gps)






