#!/usr/bin/env python

# mapper function for the first experiment in Lecture_Hadoop, CE6500C 2017

# The first experiment is to reaggregate the raw wavetronix data from 20s interval to 5min interval.
# One tricky point is that the raw wavetronix data has different data length in each row. In other words, the data is not well structured. This also makes it hard to use PIG to process the data.

# This mapper function takes in and processes the raw data line by line, finds the speed, count and occup for each lane, calculate and output the avg_speed, total_count and avg_occup with the reaggregated time as the key.

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split(',')
    # find the length of words
    l = len(words)
    # get sensor name
    sensor = words[0].strip()
    # initalize some variables
    weightedspeedsum = 0
    countsum = 0
    occupancysum = 0
    avgoccupancy = 0.0
    avgspeed = 0.0
    num_lane = 1
    
    # if the sensor is reporting data (not off or fail), we continue the calculation
    # l>6 makes sure the sensor is not off or fail, (l-6)%11==0 makes sure the data record has the right length (doesn't lost any columns)
    if l>6 and (l-6)%11==0:
        
        # find the time
        date = words[1]
        year = date[:4]
        month = date[4:6]
        day = date[6:]
        Date_newformat = month+'/'+day+'/'+year
        time = words[2]
        hour = time[:2]
        minute = time[2:4]
        second = time[4:]
        # calculate the new time in your re-aggregated interval
        # in this case we reaggregate time into 5 min intervals.
        time_interval_new = int(int(minute)/5)
    
        # update the number of lanes based on data length
        num_lane = int((l-6)/11)
    
        # loop through the data and process speed, count and occup in each lane
        for i in range(num_lane):
            count = words[i*11+7]
            speed = words[i*11+10]
            occupancy = words[i*11+9]
            # set the data quality check, replace the error values by desired values
            # you can put other auility check here, for example, sometimes the crazy sensors can report a gigantic number for count or report a negative number for speed, so you can set the upper bound and lower bound for speed, count and occup here.
            
            if count=='null':
                count = 0
            if speed=='null':
                speed = 0
            if int(speed)<0:
                speed = 0
            if occupancy=='null':
                occupancy = 0
    
            # update the total count
            countsum += int(count)
            # update the weighted total speed
            weightedspeedsum += int(count)*int(speed)
            # update the total occup
            occupancysum += int(occupancy)

    # calculate average occupancy
    avgoccupancy = occupancysum/num_lane
    # calculate weighted average speed
    if countsum>0:
        avgspeed = weightedspeedsum/1.6/countsum

    # output to STDOUT (standard output)
    # everything before the first tab is the key (as default)
    print sensor+','+Date_newformat+','+hour+','+str(time_interval_new)+'\t'+str(avgspeed)+','+str(countsum)+','+str(avgoccupancy)
    


