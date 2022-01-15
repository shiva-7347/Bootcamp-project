import tkinter as tk
import requests
from datetime import datetime
import time


def Weather(canvas):
	city = textField.get()
	api_key='792103d3309875b3705ceaf7679fb495'
	complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key
	api_link = requests.get(complete_api_link)
	api_data = api_link.json()

	#create variables to store and display data
	temp_city = ((api_data['main']['temp']) - 273.15)
	min_temp = int(api_data['main']['temp_min'] - 273.15)
	max_temp = int(api_data['main']['temp_max'] - 273.15)
	weather_desc = api_data['weather'][0]['description']
	humidt = api_data['main']['humidity']
	wind_speed = api_data['wind']['speed']
	pressure = api_data['main']['pressure']
	date_time = datetime.now().strftime("%d %b %y | %I:%M:%S %p")
	sunrise = time.strftime('%I:%M:%S', time.gmtime(api_data['sys']['sunrise'] - 21600))
	sunset = time.strftime('%I:%M:%S', time.gmtime(api_data['sys']['sunset'] - 21600))
	Tdata = "\n"+ "Min Temp: " + str(min_temp)+"°C"+"\n"+"Max Temp: "+str(max_temp) + "°C" +"\n" + "Pressure: " +str(pressure)+"\n" +"Humidity: " + str(humidt) + "\n" +"Wind Speed: " + str(wind_speed ) + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset
	label1.config(text = Tdata)

canvas = tk.Tk()
canvas.wm_iconbitmap('favicon.ico')
canvas.geometry("700x650")
canvas.title("Weather App")
canvas.configure(background = '#3f6f9e')
f = ("arial", 15, "bold")
t = ("arial", 35, "bold")
textField = tk.Entry(canvas, justify='center', width = 20, font = t)
textField.pack(pady = 20)
textField.focus()
textField.bind('<Return>', Weather)

label1 = tk.Label(canvas, font=f)
label1.pack()
canvas.mainloop()
