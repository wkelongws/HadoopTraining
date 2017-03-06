## Assignment for Lecture6_Hadoop


[//]: # (Image References)

[CDFs]: ./output/CDFs.png "CDFs"
[sensor]: ./output/sensor.png "sensor"

The dataset you need to work on in this assignment is data_CE650C/wavetronix_sample/CSV/20161231.csv in the test cluster.
This is the 5-min aggregated wavetronix data for 12/31/2016.

There is a CSV file in this assignment folder called "IWZ_Sensor_List_sample.csv".
There are three columns in this file. First column is direction; Second column is sensor name; and the last column is sensor group.

You task is to analyze the traffic speed collected by the sensors in group "1t" and direction "1" and find the sensor behaving different from others. 

(Sensors of group "1t" locates on I35 between Ames and Desmoines. You can find the geo-location of these sensors from the complete IWZ list in Exp4 repo if you want.)

####The pipeline to finish the task should look like this:

* write a PIG script to extract the traffic speed collected by sensors belonging to group "1t" and direction "1"
* draw speed profile and speed CDF for each sensor using any tool. jupyter notebook is strongly recommended because we gona use jupyter notebook for the comming lecture.

Speed profile and CDF for each sensor may look like this:
![alt text][sensor]

To identify the sensor behaving different you may want to overlay CDF for all sensors in one figure:
![alt text][CDFs]]

The final submission should include:

* the PIG script for extracting the target sensors
* a short write-up about the sensor you identified as different from others. Explain why you think the sensor behaves different.
* figures which can support your conclusion.


