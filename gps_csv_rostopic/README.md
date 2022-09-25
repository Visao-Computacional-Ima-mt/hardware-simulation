# GPS data in ROS topic

A package that transform a GPS data in a CSV format to a ROS topic in a NAVSAT/fix message. The topic publish 1 msg per second in a default dataset from USP São Carlos.

## Topic Published

The package uses Mapviz to visualize the topic being published, and five different topics. One basic topic with all the data from the dataset and another four with the correction quality from the generated fix (RTK, DGPS, Simple Fix and No fix). The list of the topics is right bellow:

```
All data: /gps/fix
fixed RTK :  /gps/fRTK/fix
Differential GPS: /gps/DGPS/fix
Simple Correction data:  /gps/simple/fix
No Correction data: /gps/no_correction/fix
```

## Running

To run the node one can use the following roslaunch command:

```console
user@pc: ~$ roslaunch gps_csv_rostopic gps.launch
```

There is the option to run the node without the launch file as bellow

```console
user@pc: ~$ rosrun gps_csv_rostopic quality_code.py
```

And there is a python script without the correction info in topics, just the data fix, to run uses the following command:

```console
user@pc: ~$ rosrun gps_csv_rostopic simple_code.py
```

## Change Dataset

If one wants to uses the same package with others dataset in CSV previously generated, just upload the file in the "csv" directory and launch the node with argument as the same name of the file. For example, if the dataset file name is "gps.csv", uses the following command:

```console
user@pc: ~$ roslaunch gps_csv_rostopic gps.launch file:="gps.csv"
```

It is important that the file is in CSV format, in other words, a "comma separated values" table and that the order of the coluns is the same as the default dataset, presented in the image bellow:

![image](https://github.com/Visao-Computacional-Ima-mt/hardware-simulation/blob/main/gps_csv_rostopic/image/table.png)

## Other details

If the Mapviz don't start with the all the topic coloured as the image bellow click in the "File" button on the left up corner and in "Open config", then select the "config2.mvc" file in the "mapviz" directory.

![image](https://github.com/Visao-Computacional-Ima-mt/hardware-simulation/blob/main/gps_csv_rostopic/image/map.png)
