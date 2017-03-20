
-- load data in with the name and data type of each column specifically defined

wavetronix = LOAD 'data_CE650C/wavetronix_sample/CSV/20161231.csv' USING PigStorage(',') AS (sensor:chararray,date:chararray,hour:int,minute5:int,speed:float,count:int,occup:float);

matchtable_raw = LOAD 'Shuo/IWZ_Sensor_List_sample.csv' USING PigStorage(',') AS (coded_direction:int,Name:chararray,Group:chararray);

-- clean data

matchtable = FILTER matchtable_raw BY (Group == '1t' AND coded_direction == 1);

-- join data

data = JOIN wavetronix BY sensor, matchtable BY Name;

-- output results

STORE data INTO 'Shuo/output_Assignment';

DUMP matchtable;
