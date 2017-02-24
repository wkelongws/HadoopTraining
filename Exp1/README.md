# Exp1 MapReduce in Python

##Re-aggregated Wavetronix data from 20s into 5min

###step1: check the input data

we will use
1 day wavetronix data downloaded and parsed from [real-time data feed](http://205.221.97.102/Iowa.Sims.AllSites.C2C/IADOT_SIMS_AllSites_C2C.asmx/OP_ShareTrafficDetectorData?MSG_TrafficDetectorDataRequest=string%20HTTP/1.1) using the techniques you applied in the first assignment

* data location:

data_CE650C/wavetronix_sample/RAW/12312016.txt

hdfs dfs -ls data_CE650C/wavetronix_sample/RAW

* check the size of the file:

hdfs dfs -du -h data_CE650C/wavetronix_sample/RAW/12312016.txt

* check how many lines are in the file:

hdfs dfs -cat data_CE650C/wavetronix_sample/RAW/12312016.txt | wc -l

* see the top 100 lines in the file:

hdfs dfs -cat data_CE650C/wavetronix_sample/RAW/12312016.txt | head -100

###step2: change your output path in job_Exp1

Open job_Exp1 in WinSCP or FileZilla

change "your/output/path" to a path you want your result in. The path has to be in your own folder so that you won't mess up with other people. For example: change "your/output/path" to "Shuo/output"

note: there are two places you need to change: 1: hdfs dfs -rmr your/output/path 2: -output your/output/path   change both!

note2: you don't need to create the path before you run your code, the output path will be automatially created by the program. Actually you have to make sure the output path does not exit before you run your program. Otherwise it will return error.


###step3: run the job

Before running the job, you need to make sure all three files: Exp1_mapper.py, Exp1_reducer.py and job_Exp1 have executive permission.

How to change the permisson:

Right click a file in WinSCP or FileZilla, choose properties or permissons, check the X or executive box under Owner (the first row)

It's time to run a job!

To run the job_Exp1, in Putty or Terminal simply type: ./job_Exp1

Let's see what happens..

###step4: Check the result

* check the output folder:

hdfs dfs -ls your/output/path

* check the size of the file:

hdfs dfs -du -h your/output/path/part-00000.txt

* check how many lines are in the file:

hdfs dfs -cat your/output/path/part-00000.txt | wc -l

compare to the number of lines in the input file, it is roughly 15 times smaller. Because we reaggregated 20s data into 5min data

* see the top 100 lines in the file:

hdfs dfs -cat your/output/path/part-00000.txt | head -100

###step5: Download the result to your machine

* download from HDFS to "Local"

hdfs dfs -copyToLocal your/output/path/part-00000

* download from "Local" to your machine

download from WinSCP from FileZilla by dragging and dropping.

* Then you can treat it using anything you want on your machine!


##step6: Create your own mapper and reducer function!

Our 5min aggregated data has {sensor, time, hour, 5min, avgspeed, totalcount, avgoccupancy}

Now we want 30min aggregated data and besides avgspeed, totalcount and avgoccupancy we also want the minimum speed.

So the new aggregated data should has {sensor, time, hour, 30min, avgspeed, totalcount, avgoccupancy, minspeed}

In this challenge you need to open and change both Exp1_mapper.py and Exp1_reducer.py

Good Luck and Have Fun!

HINT: 

    1. To change the aggregateion level, you need to change the output key in the mapper function to make sure all records belonging to the same 30min period get the same key!

    2. To get the minumum speed, in mapper you need to find the minimum speed from all lanes and output it to reducer, and then in reducer you need to find the minimum speed for each key.

### HDFS shell command

[HDFS shell command](https://hadoop.apache.org/docs/r2.4.1/hadoop-project-dist/hadoop-common/FileSystemShell.html)

hdfs dfs –ls

hdfs dfs –mkdir

hdfs dfs –copyFromLocal

hdfs dfs –du –h 

hdfs dfs –cat 

hdfs dfs –mv

hdfs dfs –put 

hdfs dfs –copyToLocal

hdfs dfs –rm

hdfs dfs -rmr
