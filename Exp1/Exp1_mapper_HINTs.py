#!/usr/bin/env python

import sys

for line in sys.stdin:
    
    line = line.strip()
    words = line.split(',')
    l = len(words)
    sensor = words[0].strip()
    
    weightedspeedsum = 0
    countsum = 0
    occupancysum = 0
    avgoccupancy = 0.0
    avgspeed = 0.0
    num_lane = 1
    
    # HINT 2: initialize a variable for tracking the lowest speed from different lanes
    ############# Your Code Here ################
    
    #############################################
    
    if l>6 and (l-6)%11==0:
        
        date = words[1]
        year = date[:4]
        month = date[4:6]
        day = date[6:]
        Date_newformat = month+'/'+day+'/'+year
        time = words[2]
        hour = time[:2]
        minute = time[2:4]
        second = time[4:]
        
        #time_interval_new = int(int(minute)/5)
        
        # HINT 1: create a new time value for each record. Since you want to reaggregate into 30min, the record within the same 30min should be assigned a same value. And the value should became (part of) your output key
        ############# Your Code Here ################
        
        #############################################
        
        num_lane = int((l-6)/11)
    
        for i in range(num_lane):
            count = words[i*11+7]
            speed = words[i*11+10]
            occupancy = words[i*11+9]

            if count=='null':
                count = 0
            if speed=='null':
                speed = 0
            if int(speed)<0:
                speed = 0
            if occupancy=='null':
                occupancy = 0

            countsum += int(count)
            weightedspeedsum += int(count)*int(speed)
            occupancysum += int(occupancy)
                
            # HINT 2: update the variable to track the lowest speed from different lanes
            ############# Your Code Here ################
                
            #############################################

    avgoccupancy = occupancysum/num_lane
    if countsum>0:
        avgspeed = weightedspeedsum/1.6/countsum


    #print sensor+','+Date_newformat+','+hour+','+str(time_interval_new)+'\t'+str(avgspeed)+','+str(countsum)+','+str(avgoccupancy)

    # HINT 1: output your key and value (separated by tab). All records within the same 30min should have the same key, and value should have avgspeed, count, occupancy and lowest speed.
    ############# Your Code Here ################

    #############################################



