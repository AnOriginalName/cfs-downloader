import sys
import datetime
import pygrib 

#This prints the list of commands to be executed in the run BASH script

variable = sys.argv[1]
step = int(sys.argv[2])
start_year = sys.argv[3]
start_month = sys.argv[4]
end_year = sys.argv[5]
end_month = sys.argv[6]
targ_lat = sys.argv[7]
targ_lon = sys.argv[8]
down_date = [int(start_year),int(start_month)] #date for the input to the download_data script
conv_date = [int(start_year),int(start_month)] #date for the input to the convert script

grbs = pygrib.open("cprat.01.2015012100.daily.grb2")
grbs.seek(0)
grb = grbs[1]
#The following finds the location closest to the target latitude and target longitude
#-----------------------------------------------------------------------------------
lats = list(set(grb['latitudes']))
lons = list(set(grb['longitudes']))
lat_index = 0
lon_index = 0
min_diff = abs(lats[0] - float(targ_lat))
if float(targ_lon) < 0:
	targ_lon = str(360 + float(targ_lon))
if float(targ_lat) > 180:
	targ_lat = str(float(targ_lat) - 360)
for i in range(1,len(lats)):
	diff = abs(lats[i] - float(targ_lat))
	if diff < min_diff:
		min_diff = diff
		lat_index = i
min_diff = abs(lons[0] - float(targ_lon))
for i in range(1,len(lons)):
	diff = abs(lons[i] - float(targ_lon))
	if diff < min_diff:
		min_diff = diff
		lon_index = i
lat = lats[lat_index]
lon = lons[lon_index]
#---------------------------------------------------------------------------------------------


# This formats the inputs to download_data and convert
#If it is for download_data, it inputs the date , step size and the variable name
# If it is for convert, it inputs the date, latitude index, longitude index, output file name, the real latitude and real longitude
# The indices are for the corresponding indices in the value array for the location. For more look to convert.py
def s_time(date, t="", file=False):
	global step
	global lat_index
	global lat
	global lon_index
	global lon

	s_year = str(date[0])
	s_month = str(date[1])
	end = ""
	if (date[1] < 10):
		s_month = "0" + s_month
	if t == "down":
		end = " " + str(step) + " " + variable
	else:
		end = " " + lat_index + " " + lon_index + " " + sys.argv[9] + " " + lat + " " + lon
	if(file == True):
		return s_year + "/"	+ s_month
	return s_year + " " + s_month + end
	


#This incrememnts the date by 1 month. 
def increment_date(date):
	date[1] += step
	if date[1] > 12:
		date[1] = step
		date[0] += 1
	return date

print("echo Forecast Date, Data Date,"  + variable  + ", latitude, longitude > " + sys.argv[9] + ".csv")


print("./download_data " + s_time(down_date,"down"))
print("wait")
down_date = increment_date(down_date)

print("./convert " + s_time(conv_date) + "| ./download_data " + s_time(down_date,"down"))
conv_date = increment_date(conv_date)
down_date = increment_date(down_date)
print("wait")

while True:
	print("./download_data " + s_time(down_date,"down") + " | ./convert " + s_time(conv_date) +" ")
	print("wait")
	if down_date[1] >= int(end_month) and down_date[0] >= int(end_year):
		break
	conv_date = increment_date(conv_date)
	down_date = increment_date(down_date)

conv_date = increment_date(conv_date)
print("./convert " + s_time(conv_date))
print("wait")
print(" ")
