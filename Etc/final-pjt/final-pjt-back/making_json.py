# -*- coding: utf-8 -*-
from pprint import pp, pprint
# from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import quote
# import json
# import re
import requests
 


url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json'
param = {
        'key' : '3d301c600964bac4f882a000de7aef26',   # 발급받은 키,
        'targetDt' : 20200101,
}
arr= []
for i in range(1,13):    
    rq = requests.get(url, params = param)
    j = rq.json()
    param['targetDt'] += 100
    # pprint(j)
    boxOfficeResult = j.get('boxOfficeResult')
    dailyBoxOfficeList = boxOfficeResult.get('dailyBoxOfficeList')
    for i in range(len(dailyBoxOfficeList)):
        
        movieNm = dailyBoxOfficeList[i].get('movieNm')
        arr.append(movieNm)
        # print(movieNm)
    # for i in range(50):
    #     arr.append(movieNm[i].get('movieNm'))
arr = list(set(arr))
# print(arr)
# print(len(arr))


import os
import sys
import requests
import time

client_id = "TQPrxWOuQObW6eIKpsO5"
client_secret = "00IUdXmw9r"
movie_data = []
for i in arr:
    time.sleep(0.5)
#네이버 영화 API 키 값
    movie=f'{i}'
    header_parms ={"X-Naver-Client-Id":client_id,"X-Naver-Client-Secret":client_secret}
    url = f"https://openapi.naver.com/v1/search/movie.json?query={movie}"
    res=requests.get(url,headers=header_parms)
    data =res.json()
    try:
        if data['items'][0]['title']:
            # print(data['items'][0])
            one_data = {}
            one_data['model'] = 'movies.movie'
            one_data['fields'] = data['items'][0]
            movie_data.append(one_data)
    except:
        pass
        
    # if data['display']:
    #     # if data['items'][0]['title'][3:-4] == movie:
    #     # movie_data.append(data['items'][0])
    #     # pprint(data['items'][0]['title'])
    #     pprint(data['items'][0]['title'])
    #         # pprint(data['items'][0]['title'][3:-4])
    #         # pprint(movie)
    
# pprint(arr)
# print(len(arr))
print(len(movie_data))
pprint(movie_data)
# with open('movie_data.json', 'w', encoding='UTF-8') as f:
#     json.dump(movie_data, f, ensure_ascii=False, indent="\t")


# result = open('movie_data.json', 'r').read()
# result = json.loads(result)
# pprint(result) 
