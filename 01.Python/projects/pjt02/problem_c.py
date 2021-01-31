import requests
from tmdb import URLMaker
from pprint import pprint


def ranking():
    maker = URLMaker('b152440d8749a910c7225ecf35b548ce')
    url = maker.get_url()
    response = requests.get(url).json()
    
    # vote_average 키를 기준으로, 내림차순으로 response를 정렬
    sorted_movie = sorted(response['results'], key=lambda x: x['vote_average'], reverse=True)
    # 내림차순이므로 앞에서부터 5번째 영화까지 슬라이싱하여 반환
    return sorted_movie[:5]
        

if __name__ == '__main__':
    # popular 영화 평점순 5개 출력
    pprint(ranking())