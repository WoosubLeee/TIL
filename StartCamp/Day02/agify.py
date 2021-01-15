import requests

url = "https://api.agify.io?name=woosub"
response = requests.get(url).json()
name = response['name']
age = response['age']

print(f'저는 {name}이고, 나이는 {age}세 입니다.')