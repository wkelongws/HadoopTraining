# Exp3 Process weather using Pig

##Find maximum temperature and maximum precipitation every half an hour for a given gid using weather data

###step1: check the input data

we will use
1 day weather data

data location:

data_CE650C/weather_sample/CSV/20161231

hdfs dfs -ls data_CE650C/weather_sample/CSV

* check the size of the file:

hdfs dfs -du -h data_CE650C/weather_sample/CSV/20161231

* check how many lines are in the file:

hdfs dfs -cat data_CE650C/weather_sample/CSV/20161231 | wc -l

* see the top 100 lines in the file:

hdfs dfs -cat data_CE650C/weather_sample/CSV/20161231 | head -100

###step2: change your input and output path and run the job

download stats_for_selected_gid.pig from github

open it using any text editor and let's take a look..'

 

###step3: change your input and output path and run the job

**CHANGE and DOUBLE CHECK the INPUT PATH and OUTPUT PATH in the .pig file.**

upload stats_for_selected_gid.pig to the sever (or "Local") in your own folder.

run the pig file by typing:

pig path/to/the/pigfile/stats_for_selected_gid.pig

If the pig file is in your current working directory, just type: pig stats_for_selected_gid.pig

Note: make sure stats_for_selected_gid.pig has executive permission.

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

###step5: Optional: Download the result to your machine


##step6: Customize the code

task1: change the code to output min, max and median of each numerical feature for every hour, every 3 hours and every 8 hours

task2: CHALLENGE! output 95 percentile of each numerical feature for every hour.

Good Luck and Have Fun!

### Pig Latin resource

[Pig Latin Basics](https://pig.apache.org/docs/r0.11.1/basic.html)

[Pig built-in functions](https://pig.apache.org/docs/r0.11.1/func.html)

