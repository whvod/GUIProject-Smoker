from datetime import datetime
import time
import json
import requests

OPEN_WEATHER_API_KEY = 'd0d85f94f0538f4f938a8d2c42ac5625'
zipcode = "28677"
URL = "http://api.openweathermap.org/data/2.5/forecast?q=" + zipcode + "&appid=" + OPEN_WEATHER_API_KEY
json_data = requests.get(URL).json()
t=0

def getTemperature(int: t):
	# t = 0 is today, t=1 tomorrow t=2 overmorrow
	URL = "http://api.openweathermap.org/data/2.5/forecast?q=" + zipcode + "&appid=" + OPEN_WEATHER_API_KEY

	temp = round((json_data['list'][t]['main']['temp'] - 273.15) * (9/5) + 32)
	print('temperature is:', temp)
	now = time.asctime( time.localtime(time.time()) )
	print(now)
	
	return temp
	
if __name__ == '__main__':
	getTemperature(0)
