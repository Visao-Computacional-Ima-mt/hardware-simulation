#!/usr/bin/env python3

from hashlib import new
import numpy as np
import pandas as pd
import rospy                                                                 
from std_msgs.msg import String               
from sensor_msgs.msg import NavSatFix     
import sys   
import csv
import os

# /home/alceu/catkin_ws/src/gps_csv_rostopic/csv

path = os.path.dirname(__file__).split("/")
path[-1] = 'csv'
path = '/'.join(path)

args = rospy.myargv(argv=sys.argv)
if len(args) < 3:
    database = 'Teste2.csv'
else:
    database = args[1]


rows = []
#data = pd.read_csv("Teste2.csv")

with open(path  + "/" + database, 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)

    i=1
    #print(header,'\n')

    for row in csvreader:
        rows.append(row)
        if i <= 10:
            #print('Line',i,' = ',row)
            print('Time = ',row[1])
            print('Latitude = ',row[2])
            print('Longitude = ',row[3])
            print('Altitude = ',row[4],'\n')
        i = i + 1

print('Number of lines = ',len(rows))
print('Dimensions = ',np.shape(rows))
print('Type = ',type(rows))
#print('\n',data)

#print(header)
#print(rows)
#print(rows)
#print('\n','\n','First line = ',rows[:,1])

