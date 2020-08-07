import sys
import datetime
import pygrib

def increment_time(time):
	return time + datetime.timedelta(hours=6)

grbs = pygrib.open(sys.argv[1])
grbs.seek(0)
grb = grbs[1]
year = grb['year']
month = grb['month']
day = grb['day']
hour = grb['hour']
minute = grb['minute']
second = grb['second']
f_date = grb['dataDate']
min_lat_i = int(sys.argv[2])
min_lon_i = int(sys.argv[3])
lat = float(sys.argv[4])
lon = float(sys.argv[5])
date = datetime.datetime(year,month,day,hour)
original = date
for grb in grbs:
	#Forecast Date, Data Date, 2mm, latitude, longitude
	vals = grb['values']
	print(str(date) + ", " +  str(original) + ", ", end = " ")
	print(float(vals[min_lat_i][min_lon_i]),end = " ")
	print( ", " + str(lat) + ", " + str(lon))
	date = increment_time(date)

