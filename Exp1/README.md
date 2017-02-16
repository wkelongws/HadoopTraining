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

###step2: change

Open job_Exp1 in WinSCP or FileZilla

change "your_output_path" to a path you want your result in. The path has to be in your own folder so that you won't mess up with other people. For example: change "your_output_path" to "Shuo/output"

note: you don't need to create the path before you run your code, the output path will be automatially created by the program. Actually you have to make sure the output path does not exit before you run your program. Otherwise it will return error.


###step3: run the job

before running the




###step4: cd to your folder and check the files

ls
cd /path/to/your/folder
ls

###step5: Create your folder in HDFS

check what's in the HDFS now: 

hdfs dfs -ls

Create a folder using the same name of the folder you just created on "Local"

hdfs dfs -mkdir yourfoldername

check what's in the HDFS now:

hdfs dfs -ls

upload Exp1_mapper.py, Exp1_reducer.py and job_Exp1 to your folder in HDFS

hdfs dfs -copyFromLocal Exp1_mapper.py yourfoldername
hdfs dfs -copyFromLocal Exp1_reducer.py yourfoldername
hdfs dfs -copyFromLocal job_Exp1.py yourfoldername

Check what's in your HDFS folder now

hdfs dfs -ls yourfoldername

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
