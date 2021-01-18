import requests

key = 'mbsr22ZxsnSdYzgWL6ZEXF8zchZReHHj06FVrZEaYhzLx14roDMN0DLdr%2FCNzC4K5i1s3UmmeNZ3VEvoGtg0%2BQ%3D%3D'

url = f'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={key}&numOfRows=10&pageNo=2&sidoName=서울&ver=1.0&returnType=json'
response = requests.get(url).json()
print(response.get('response').get('body').get('items'))
item = response.get('response').get('body').get('items')[9]
time = item.get('dataTime')
station = item.get('stationName')
dust = int(item.get('pm10Value'))

print(f'{time} 기준 {station}의 미세먼지 농도는 {dust}입니다.')

# dust 변수에 들어 있는 값을 기준으로 상태 정보를 출력해보세요.