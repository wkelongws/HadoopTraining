
-- load data in with the name and data type of each column specifically defined

weather = LOAD 'Shuo/weatherCSV/2016/201612/20161231' USING PigStorage(',') AS (time:chararray,gid:int,tmpc:float,wawa:chararray,ptype:int,dmpc:chararray,smps:chararray,drct:int,vsby:chararray,roadtmpc:chararray,rad:chararray,snwd:chararray,pcpn:float);

-- remove other gids, only keep gid 1000

gid1000 = FILTER weather BY gid == 1000;

-- extract gid, temprature, precipitation, hour and half hour.

gid1000_halfhour = FOREACH gid1000 GENERATE gid, tmpc, pcpn, ToString(ToDate(time, 'yyyy-MM-dd HH:mm'),'yyyy-MM-dd HH') AS hour, GetMinute(ToDate(time, 'yyyy-MM-dd HH:mm'))/30 As half;

-- group data hour and half hour.

HalfHourly = GROUP gid1000_halfhour BY (gid, hour, half);

-- lower case 'group' stands for the key as default. Apply aggregation function and get the result

data = FOREACH HalfHourly GENERATE group.gid, group.hour, group.half, MAX(gid1000_halfhour.tmpc), MAX(gid1000_halfhour.pcpn);

-- save the result

-- STORE data INTO 'Shuo/testoutput' USING PigStorage(',');

-- truncate result for display

-- dataout = LIMIT data 100;


-- sort the output data by time in desired order
dataout = ORDER data BY hour ASC, half ASC;

-- display data
dump dataout;
