# Exp0

##Login and upload files to HDFS

###step1: Login Test Cluster through WinSCP or FileZilaa

Open WinSCP (windows) or FileZilla (mac)

User1, User2, User3, User4, User5, User6, User7 		– 10.29.19.6
User8, User9, User10, User11, User12, User13, User14 	– 10.29.19.10
Others 								– 10.29.19.11

Username: class
Password: hadoop

###step2: Create your own folder and upload files

Create a folder using your name or any name you want in WinCSP or FileZilla
(This is equivalent to using shell command “mkdir”)

Download Exp1_mapper.py, Exp1_reducer.py and job_Exp1, and upload the three files to the folder you just created on the test cluster.

###step3: Login Test Cluster through Putty or Terminal

Open Putty (windows) or Terminal (mac)

same login credentials with WinSCP/FileZilla

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
