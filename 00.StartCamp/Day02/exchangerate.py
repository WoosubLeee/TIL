from bs4 import BeautifulSoup
import requests

url = "https://finance.naver.com/marketindex/"
response = requests.get(url).text
soup = BeautifulSoup(response, 'html.parser')
rate = soup.select_one("#exchangeList > li:nth-child(1) > a.head.usd > div > span.value")

print(f'{rate.text}는 환율입니다.')