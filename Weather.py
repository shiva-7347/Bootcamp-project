import requests
from datetime import datetime

api_key='792103d3309875b3705ceaf7679fb495'
location = input("Enter Your City Name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
humidt = api_data['main']['humidity']
wind_speed = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %y | %I:%M:%S %p")

#printing of data on consloe
print("---------------------------------------------------------")
print("Weather stats for - {} || {} ".format(location.upper(), date_time))
print("---------------------------------------------------------")

print("Current Temperature id      : {:.2f}deg C".format(temp_city))
print("Current Weather description :",weather_desc)
print("Current Humidity            : {} %".format(humidt))
print("Current wind speed          : {} kmph".format(wind_speed))

#opening the file
f = open("Weather.txt","a+")
f.write("---------------------------------------------------------\n")
f.write("Weather stats for - {} || {} \n".format(location.upper(), date_time))
f.write("---------------------------------------------------------\n")

f.write("Current Temperature id      : {:.2f}deg C\n".format(temp_city))
f.write("Current Weather description : {}\n".format(weather_desc))
f.write("Current Humidity            : {} %\n".format(humidt))
f.write("Current wind speed          : {} kmph\n".format(wind_speed))
f.close()
