import requests

TOKEN = '1564598223:AAG_bD0Tssox0Zkj_dikUzTNJD2rsPFgAvU'
CHAT_ID = '1165363053'
url = f'https://api.telegram.org/bot{TOKEN}'

searchUrl = 'https://www.metaweather.com/api/location/search/?query=seoul'
searchResponse = requests.get(searchUrl).json()
woeid = searchResponse[0]['woeid']

weatherUrl = f'https://www.metaweather.com/api/location/{woeid}'
response = requests.get(weatherUrl).json()
title = response['title']
info = response['consolidated_weather'][0]
date = info['applicable_date']
state = info['weather_state_name']
tempNow = round(info['the_temp'], 1)
tempMax = round(info['max_temp'], 1)
tempMin = round(info['min_temp'], 1)

text = f'{title}의 {date} 날씨는 {state}이며 현재 기온은 {tempNow}°C, 최고 기온은 {tempMax}°C, 최저 기온은 {tempMin}°C입니다.'
message_url = f'{url}/sendMessage?chat_id={CHAT_ID}&text={text}'

print(requests.get(message_url))