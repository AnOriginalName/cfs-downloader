# cfs-downloader
This is a script which downloads and extracts data for 9 month forecasts from the Climate Forecast System's Time-Series found [here](https://www.ncei.noaa.gov/data/climate-forecast-system/access/operational-9-month-forecast/time-series/). The datasets are large and so it can be difficult to extract just a small portion of it. The output is a csv file. The script runs the processes in parallel, but it will still take many days to process and extract the data depending on how fast your machine is. 

## Software Requirements:
To run this program you need Python 3, the pygrib and datetime libraries installed on Python 3, as well as wget. 

## Input:
To run this program simply execute the run program with the following 9 arguments:

- Arg 1 is the target variable. This will be the variable you want to extract from the time series. The list of valid data types and exact spellings are found at the end of the readme. Probably the most interesting are tmin tmax and tmp2mm . 
- Arg 2 is the time step size in months. The program works by downloading the data a few months at a time, extracting and saving the values requested to a csv file. Then, it deletes the downloaded data and then downloads the next few months of data. One month of data is around 25 Gigabytes, so you should adjust the step size to accomodate your disk space.
- Arg 3 is the start year
- Arg 4 is the start month These should be in the format: 2017 02, the month should always be 2 digits. 
- Arg 5 is the end year
- Arg 6 is the end month
- Arg 7 is the target latitude 
- Arg 8 is the target Longitude: Arg 7 and 8 are the target location, the project includes one grb file. This is used to calculate the closest location to the target location within the data. Thus, the output latitude and longitude will be different from the target location, but as close as possible.
- Arg 9 is the name of the output file. The output will be a csv file, so this will be the name of the file.

## Output:
The data is written out as a csv file with the following Columns:
Forecast Date: This is the date that is being forecasted for. 
Data Date: This is the date that the forecast was made
(Value): This is replaced by whatever data type was inputed. 
Latitiude: This is the real latitude, the closest latitude to the target latitude within the data
Longitude: This is the real longitude, the closest longitude to the target longitude within the data

Depending on how long the time period is, the csv file will be huge, probably better for use in reading within a script than manual viewership. 

## File Descriptons:
run.py: 
run: This runs `run.py` with the aforementioned arguments, puts the output into a txt file called `commands.txt`, then evaluates each line as a BASH command.
download_data.py:  

## Valid Data Types: 
- chi200
- chi850
- cprat
- csdlf
- csdsf
- csusf
- dlwsfc
- dswsfc
- gflux 
- icecon
- icethk
- ipv450
- ipv550
- ipv650
- lhtfl
- nddsf
- ocndt2
- ocndt5c
- ocndt10c
- ocndt15c
- ocndt20c
- ocndt25c
- ocndt28c 
- ocnheat
- ocnmld
- ocnsal5
- ocnsal15
- ocnsild
- ocnslh
- ocnsst
- ocnt15
- ocntchp
- ocnu5
- ocnu15
- ocnv5
- ocnv15
- ocnvv55
- prate
- pressfc
- prmsl
- psi200
- psi850
- pwat
- q2m
- q500
- q700
- q850
- q925
- runoff
- shtfl
- snohf
- soilm1
- soilm2
- soilm3
- soilm4
- soilt1
- t2
- t50
- t200
- t250
- t500
- t700
- t850
- t1000
- tcdcclm 
- tmax
- tmin
- tmp2m
- tmphy1
- tmpsfc
- ulwsfc
- ulwtoa
- uswsfc
- uswtoa
- vddsf
- vvel500
- weasd
- wnd10m
- wnd200
- wnd250
- wnd500
- wnd700
- wnd850
- wnd925
- wnd1000
- wndstrs
- z200
- z500
- z700
- z850
- z1000
