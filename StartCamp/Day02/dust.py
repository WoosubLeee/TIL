import requests
from pprint import pprint

apiKey = "bBzsxh9wqp3C%2FfLYAkLqCwXRps3wxo%2F4jMJgOmttcqrWeaGSBNT5LTWpp7trJxgBsOvJeUMkdPmJThPqoQX1FA%3D%3D"
url = f"http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={apiKey}&returnType=json&numOfRows=100&pageNo=1&sidoName=%EC%84%9C%EC%9A%B8&ver=1.0"
response = requests.get(url).json()
items = response['response']['body']['items']

for i in items:
    station = i['stationName']
    if station == "서대문구":
        time = i['dataTime']
        pm10 = int(i['pm10Value'])
        pm25 = i['pm25Value']
        if pm10 > 150:
            grade = '매우나쁨'
        elif pm10 > 80:
            grade = '나쁨'
        elif pm10 > 30:
            grade = '보통'
        else:
            grade = '좋음'
        print(f'{time} 기준 {station}의 PM10 값은 {pm10}이고, PM2.5 값은 {pm25}으로 {grade} 수준입니다.')