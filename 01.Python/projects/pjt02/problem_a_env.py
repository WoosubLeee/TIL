import requests
from tmdb import URLMaker
from decouple import config

TMDB_API_KEY = config('TMDB_API_KEY')

def popular_count():
    # API key 값 적용하여 URLMaker 클래스 생성
    maker = URLMaker(TMDB_API_KEY)
    url = maker.get_url()
    # json 형식의 응답을 딕셔너리로 변환
    response = requests.get(url).json()
    return len(response['results'])


if __name__ == '__main__':
    print(popular_count())