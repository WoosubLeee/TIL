import requests
from pprint import pprint

searchUrl = 'https://www.metaweather.com/api/location/search/?query=seoul'
searchResponse = requests.get(searchUrl).json()
woeid = searchResponse[0]['woeid']

url = f'https://www.metaweather.com/api/location/{woeid}'
response = requests.get(url).json()
title = response['title']
info = response['consolidated_weather'][0]
date = info['applicable_date']
state = info['weather_state_name']
tempNow = round(info['the_temp'], 1)
tempMax = round(info['max_temp'], 1)
tempMin = round(info['min_temp'], 1)

print(f'{title}의 {} 날씨는 {state}이며 현재 기온은 {tempNow}°C, 최고 기온은 {tempMax}°C, 최저 기온은 {tempMin}°C입니다.')