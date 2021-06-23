import requests
from datetime import datetime

api_key = '279431890e38f7a16867c538788c10ad'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()


temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print ("-------------------------------------------------------------")
print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
print ("-------------------------------------------------------------")

print ("Current temperature is: {:.2f} ℃".format(temp_city))
print ("Current weather desc  :",weather_desc)
print ("Current Humidity      :",hmdt, '%')
print ("Current wind speed    :",wind_spd ,'kmph') 

file = open('Weather Report.txt', 'w', encoding='utf-8') 
file.write("-------------------------------------------------------------")
file.write("\nWeather Report : {}  || {}".format(location.upper(), date_time))
file.write("\n-------------------------------------------------------------")
file.write(f"\nCurrent temperature :    {temp_city:.2f} "+ "℃" + "\nCurrent weather desc :  " + str(weather_desc) + "\nCurrent Humidity :  "+ str(hmdt) +"%" + "\nCurrent wind speed :  " + str(wind_spd)+ " kmph")
