# Lecture6

###In this lecture we are going to learn what is Hadoop and how to perform parallel computing using hadoop.

###After this lecture you should be able to:

* understand the structure of HDFS, how files are stored in HDFS and how to exchange files with HDFS;
* understand how MapReduce works and run your own MapReduce program written in python using Hadoop streaming utility;
* write you own PIG script to solve data processing problems in your class project and future research.

###Here are something you need to prepare before the class:

[//]: # (Image References)

[HDFSin]: ./figures_support/HDFSin.png "HDFSin"
[Putty]: ./figures_support/Putty.png "Putty"
[Puttyin]: ./figures_support/Puttyin.png "Puttyin"
[Puttylogin]: ./figures_support/Puttylogin.png "Puttylogin"
[WinSCP]: ./figures_support/WinSCP.png "WinSCP"
[WinSCPlogin]: ./figures_support/WinSCPlogin.png "WinSCPlogin"
[FileZilla]: ./figures_support/FileZilla.png "FileZilla"
[FileZillain]: ./figures_support/FileZillain.png "FileZillain"
[FileZillalogin]: ./figures_support/FileZillalogin.png "FileZillalogin"
[mac1]: ./figures_support/mac1.png "mac1"
[mac2]: ./figures_support/mac2.png "mac2"
[mac3]: ./figures_support/mac3.png "mac3"
[mac4]: ./figures_support/mac4.png "mac4"
[mac5]: ./figures_support/mac5.png "mac5"

## Required: 

We will be using INTRANS test cluster in this lecture, but you need to install some software on your laptop to support the connection to the cluster.

##**Windows:**

1. Putty 
![alt text][Putty]
2. WinSCP
![alt text][WinSCP]

##**Mac:**

1. FileZilla
![alt text][FileZilla]

###Please search online, download and install the required sofeware according to you laptop system. Then let's try to connnect to the cluster and HDFS:

##**Windows:**

* Connet to cluster:

1. open Putty and login
    ![alt text][Puttylogin]
    
2. type -ls to check the file on local machine (suppose you logged in 10.29.19.10 then 10.29.19.10 is your local machine, which is part of the cluster and we will discuss the whole structure in class) We have three folders and three files on local right now:
    ![alt text][Puttyin]

* exchange file with cluster:

1. open WinSCP and login
    ![alt text][WinSCPlogin]
    
2. WinSCP provide a save file exchange platform between your laptop and the remove linux machine. The left window is your laptop, the right window is the remove linux machine you logged in (in this case it is 10.29.19.10 which we also call it "local" or "server" or "cluster" in different situations.....) You can upload files from you laptop to the cluster by simply dragging and dropping files to the right window, and you can download files to you laptop from the cluster by simply dragging and dropping files from the right window.
    This is the way I upload the three files shown in the picture
    ![alt text][WinSCPin]

* The "Local" or "server" is not actually HDFS and the three folders and three files you have seen are not in HDFS.You can peek the files in HDFS by typing "hdfs dfs -ls" in Putty command line
    ![alt text][HDFSin]
    We will explore HDFS more in the class!


##**Mac:**

* Connet to cluster:

1. open Terminal and type "ssh username@URL"
    ![alt text][mac1]

2. input password
    ![alt text][mac2]
    
3. you are in! easy
    ![alt text][mac3]
    
4. type -ls to check the file on local machine (suppose you logged in 10.29.19.10 then 10.29.19.10 is your local machine, which is part of the cluster and we will discuss the whole structure in class) We have three folders and three files on local right now.
    ![alt text][mac4]

* exchange file with cluster:

1. open FileZilla and login: type URL in host, username, password and 22 in port:
    ![alt text][FileZillain]
    
2. FileZilla provide a save file exchange platform between your mac and the remove linux machine. The left window is your mac, the right window is the remove linux machine you logged in (in this case it is 10.29.19.10 which we also call it "local" or "server" or "cluster" in different situations.....) You can upload files from you laptop to the cluster by simply dragging and dropping files to the right window, and you can download files to you laptop from the cluster by simply dragging and dropping files from the right window. This is the way I upload the three files shown in the picture
    ![alt text][FileZillalogin]

* The "Local" or "server" is not actually HDFS and the three folders and three files you have seen are not in HDFS. You can peek the files in HDFS by typing "hdfs dfs -ls" in Terminal command line
    ![alt text][mac5]
    We will explore HDFS more in the class!



Jupyter notebook

* Optional: 
Eclipse
Java


* more options:
Virtual machine (Cloudera)
Cloud service





