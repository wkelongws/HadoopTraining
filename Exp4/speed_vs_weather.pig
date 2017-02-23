
-- load data in with the name and data type of each column specifically defined

weather_raw = LOAD 'data_CE650C/weather_sample/CSV/20161231' USING PigStorage(',') AS (time:chararray,gid:int,tmpc:chararray,wawa:chararray,ptype:int,dmpc:chararray,smps:chararray,drct:int,vsby:chararray,roadtmpc:chararray,rad:chararray,snwd:chararray,pcpn:chararray);

wavetronix_raw = LOAD 'Shuo/output_Exp1/part-00000' USING PigStorage(',') AS (sensor:chararray,date:chararray,hour:int,minute5:int,speed:float,count:int,occup:float);

matchtable_raw = LOAD 'Shuo/IWZ_Sensor_List_withGID.csv' USING PigStorage(',') AS (Direction:chararray,coded_direction:chararray,IWZ:chararray,Latitude:chararray,Longitude:chararray,Name:chararray,SegmentLength:chararray,Group:chararray,Group_new:chararray,ID:chararray,LinearReference:chararray,order:chararray,ProjectName:chararray,Portable:chararray,APS:chararray,Device:chararray,GID:int);

-- clean data

matchtable = FILTER matchtable_raw by Group_new == 'Group 1 - 1.3 - I80';

targetgroup = FOREACH matchtable GENERATE Name, GID;

wavetronix = FOREACH wavetronix_raw GENERATE sensor, hour, minute5, speed;

weather = FOREACH weather_raw GENERATE gid, GetHour(ToDate(time, 'yyyy-MM-dd HH:mm')) AS hour, GetMinute(ToDate(time, 'yyyy-MM-dd HH:mm'))/5 AS minute5, tmpc, pcpn;


-- join data

firstjoin = JOIN wavetronix BY sensor, targetgroup BY Name;

secondjoin = JOIN firstjoin BY (GID, hour, minute5), weather BY (gid, hour, minute5);

data = FOREACH secondjoin GENERATE wavetronix::hour, wavetronix::minute5, wavetronix::sensor, wavetronix::speed, weather::gid, weather::tmpc, weather::pcpn;


-- output results

dataout = LIMIT data 100;

dump dataout;

STORE data INTO 'Shuo/testoutput2';
