# Exp2 Hourly avgspeed of Inrix using Pig

##Find hourly average speed using Inrix data

###step1: check the input data

we will use
1 day weather data and your reaggregated 5min wavetronix data from Experiment 1

data location:

weather:
data_CE650C/weather_sample/CSV/20161231

and 
wavetronix:
your/output/path/part-00000.txt

If you lost the reaggreagted 5min wavetronix data you can quickly rerun the code in Exp1


###step2: change your input and output path and run the job

download speed_vs_weather.pig and IWZ_Sensor_List_withGID.csv from github

open it and let's take a look..'

 

###step3: change your input and output path and run the job

upload speed_vs_weather.pig and IWZ_Sensor_List_withGID.csv to the sever (or "Local") in your own folder.

Then you also need to upload IWZ_Sensor_List_withGID.csv from 'Local' to HDFS so that the pig program can read it.

hdfs dfs -copyFromLocal local/path/IWZ_Sensor_List_withGID.csv path/on/hdfs

**CHANGE and DOUBLE CHECK the INPUT PATH and OUTPUT PATH in the .pig file.**

run the pig file by typing:

pig path/to/the/pigfile/speed_vs_weather.pig

If the pig file is in your current working directory, just type: pig speed_vs_weather.pig

Note: make sure InrixAggregator.pig has executive permission.

Let's see what happens..

###step4: Check the output

* check the output folder:

hdfs dfs -ls your/output/path

* check the size of the file:

hdfs dfs -du -h your/output/path/part-00000.txt

* check how many lines are in the file:

hdfs dfs -cat your/output/path/part-00000.txt | wc -l

* see the top 100 lines in the file:

hdfs dfs -cat your/output/path/part-00000.txt | head -100

###step5: Download the result to your machine

hdfs dfs -copyToLocal your/output/path/on/HDFS your/Local/path

##step6: Use what you learnt in your project

Good Luck and Have Fun!

### Pig Latin resource

[Pig Latin Basics](https://pig.apache.org/docs/r0.11.1/basic.html)

[Pig built-in functions](https://pig.apache.org/docs/r0.11.1/func.html)

