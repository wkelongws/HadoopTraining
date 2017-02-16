#!/usr/bin/env python

# reducer function for the first experiment in Lecture_Hadoop, CE6500C 2017

# The first experiment is to reaggregate the raw wavetronix data from 20s interval to 5min interval.
# One tricky point is that the raw wavetronix data has different data length in each row. In other words, the data is not well structured. This also makes it hard to use PIG to process the data.

# This reducer function takes in and processes the output from mapper line by line, finds the speed, count and occup for each 20s, calculate and output the avg_speed, total_count and avg_occup for 5min.

# People who use java for hadoop before may have difficulties in understanding this code..
# When we say reducer (mapper also) there are two different meanings: "reducer task" and "reducer machine"
# If you have 100 different keys outputed from mapper, then you have 100 reducer tasks
# If you have 8 physical machines then you have 8 reducer machines (up to 8)
# So if you write java, the reducer program is for a renducer task and the program can only see 1 key.
# If you use hadoop streaming, the reducer program is for a reducer machine. The program will see a sorted list of keys and needs the "current_key" to check whether you have moved to the next key as shown in this code.

from operator import itemgetter
import sys

# initial vaiables
current_key = None
totalcount = 0
totalspeed = 0.0
totaloccupancy = 0.0
num = 0

# input comes from STDIN
for line in sys.stdin:
    
    # remove leading and trailing whitespace
    line = line.strip()
    
    # parse the input we got from mapper.py
    key, value = line.split('\t')
    speed,count,occupancy = value.split(',')

    # if current_key == key, it means we haven't done with it, and we need to keep updating the variables
    if current_key == key:
        totalcount += int(count)
        totalspeed += float(speed)
        totaloccupancy += float(occupancy)
        num += 1
    # if current_key ~= key, it means we have done with it, and we need to output the result and reset the variables
    else:
        # "if current_key" ensures that we don't output at the very beginning.
        if current_key:
            # write result to STDOUT
            meanspeed = 0.0
            if totalcount>0:
                meanspeed = totalspeed/totalcount
            meanoccupancy = totaloccupancy/num
            print key+','+str(meanspeed)+','+str(totalcount)+','+str(meanoccupancy)
        current_key = key
        totalcount = int(count)
        totalspeed = float(speed)
        totaloccupancy = float(occupancy)
        num = 1

# At last we need to output the result for the last key.
if current_key == key:
    meanspeed = 0.0
    if totalcount>0:
        meanspeed = totalspeed/totalcount
    meanoccupancy = totaloccupancy/num
    print key+','+str(meanspeed)+','+str(totalcount)+','+str(meanoccupancy)



