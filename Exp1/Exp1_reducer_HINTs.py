#!/usr/bin/env python

from operator import itemgetter
import sys

current_key = None
totalcount = 0
totalspeed = 0.0
totaloccupancy = 0.0
num = 0

# HINT 2: Initialize a variable for tracking the lowest speed for each key
############# Your Code Here ################

#############################################

for line in sys.stdin:
    
    line = line.strip()
    key, value = line.split('\t')
    #speed,count,occupancy = value.split(',')
    
    # HINT 2: split your value
    ############# Your Code Here ################
    
    #############################################

    if current_key == key:
        totalcount += int(count)
        totalspeed += float(speed)
        totaloccupancy += float(occupancy)
        num += 1
    
        # HINT 2: update the variable to track the lowest speed for each key
        ############# Your Code Here ################
    
        #############################################

    else:
        if current_key:
            meanspeed = 0.0
            if totalcount>0:
                meanspeed = totalspeed/totalcount
            meanoccupancy = totaloccupancy/num
            # print key+','+str(meanspeed)+','+str(totalcount)+','+str(meanoccupancy)

            # HINT 2: output your results including the lowest speed
            ############# Your Code Here ################

            #############################################

        current_key = key
        totalcount = int(count)
        totalspeed = float(speed)
        totaloccupancy = float(occupancy)
        num = 1

        # HINT 2: reset the variable for tracking the lowest speed for the next key
        ############# Your Code Here ################

        #############################################

if current_key == key:
    meanspeed = 0.0
    if totalcount>0:
        meanspeed = totalspeed/totalcount
    meanoccupancy = totaloccupancy/num
    #print key+','+str(meanspeed)+','+str(totalcount)+','+str(meanoccupancy)

    # HINT 2: output your result including the lowest speed for the last key
    ############# Your Code Here ################

    #############################################



