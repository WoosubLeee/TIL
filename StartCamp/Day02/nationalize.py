import requests

url = "https://api.nationalize.io?name=sub"
response = requests.get(url).json()
name = response['name']
print(f'저는 {name}입니다.')
for i in response['country']:
    id = i['country_id']
    prob = round(float(i['probability'])*100, 1)
    print(f'국가 : {id}, 확률 : {prob}%')

#print(f'저는 {name}이고, 나이는 {age}세 입니다.')