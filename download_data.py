import sys
import wget
import urllib.request,urllib.parse,urllib.error

year = int(sys.argv[1])
end = year + 1
day = 1
goal_month = str(sys.argv[2])
step = int(sys.argv[3])
month = int(sys.argv[2]) - step + 1
months_len = [31,28,31,30,31,31,30,31,31,30,31,30,31]
hours = ['00', '06', '12', '18']
hours_index = 0
datatype = str(sys.argv[4])

def leap_year(year):
	return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def add_day():
	global day
	global months_len
	global month
	global year

	day += 1
	if day > months_len[month-1]:
		if month == 1 and leap_year(year) and day == 29:
			return
		month += 1
		day = 1
		if month > 12:
			month = 1
			year += 1

def add_hour():
	global hours_index

	hours_index += 1
	if hours_index > 3:
		hours_index = 0
		add_day()


def day_str(n):
	global day
	global month
	global year
	global hours_index
	res = str(year)

	if n >= 2 and month < 10:
		res += '0'
	if n >= 2:
		res += str(month)
	if n >= 3 and day < 10:
		res += '0'
	if n >= 3:
		res += str(day)
	if n >= 4:
		res += hours[hours_index]
	return res

url = "https://www.ncei.noaa.gov/data/climate-forecast-system/access/operational-9-month-forecast/time-series"
ex ="https://www.ncei.noaa.gov/data/climate-forecast-system/access/operational-9-month-forecast/time-series/2015/201501/20150121/2015012100/cprat.01.2015012100.daily.grb2"
def download_types():
	global day
	global month
	global year
	global url
	global hours_index
	str_month = goal_month
	down_source = url + "/" + day_str(1) + "/" + day_str(2) + "/" + day_str(3) + "/" + day_str(4) + "/" + datatype + ".01." + day_str(4) +".daily.grb2"
	dest = "data"

	#So there are two versions of using wget here. The first has a timeout in case the internet goes down and is executed in Bash, the second does it in Python. 
	#The Bash commands have a timeout, and keeps trying to download a file if the internet goes down. 
	#However it seems to mess with the parallization, whereas the python Wget avoids issues. But there doesn't seem to be an option to keep trying if the internet goes down in the python version
	targ = dest +  "/" + str(year) + "/" +  str_month + "/" + datatype + ".01." + day_str(4) +".daily.grb2"
	#print("while true;do")
	#print("\twget  -T 15 -c " + down_source + " -O " + targ + " && break")
	#print("done")
	try:
		wget.download(down_source, targ)
	except urllib.error.HTTPError:
		print("\n------------------------------------------")
		print("FAILED TO DOWNLOAD: " + datatype + " for " + dat_str(4))
		print("------------------------------------------")

while year != end and month <= int(goal_month):
	download_types()
	add_hour()

