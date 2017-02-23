
-- load data in with the name and data type of each column specifically defined

Inrix_withHeader = LOAD 'InrixSegments/2016/12/12-31-2016.csv' USING PigStorage(',') AS (XD:int,missing1:chararray,missing2:chararray,score:int,speed1:int,speed2:int,speed3:int,traveltime:float,timestamp:chararray);

-- remove the header in the first row using pig filter function

Inrix = FILTER Inrix_withHeader BY XD > 0;

-- only extract XD, speed1, and timestamp. Convert timestamp to another format using Pig DateTime object. In this case, we throw away minute and seconds so that we can group data by hour later

XD_speed_time = FOREACH Inrix GENERATE XD, speed1, ToString(ToDate(CONCAT (SUBSTRING(timestamp, 0, 10), ' ', SUBSTRING(timestamp, 11, 19)), 'yyyy-MM-dd HH:mm:ss'),'yyyy-MM-dd HH') AS hour;

-- group data by XD and hour. Here in mapreduce thinking: mapper create XD and hour as key, then reducer work on each key.

Hourly = GROUP XD_speed_time BY (XD, hour);

-- lower case 'group' stands for the key as default. Apply aggregation function and get the result

data = FOREACH Hourly GENERATE group.XD, group.hour, AVG(XD_speed_time.speed1);

-- save the result

STORE data INTO 'Shuo/testoutput' USING PigStorage(',');

-- truncate result for display

dataout = LIMIT data 100;

-- display data
dump dataout;
