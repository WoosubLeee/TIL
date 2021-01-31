import requests
from tmdb import URLMaker
from pprint import pprint


def vote_average_movies():
    maker = URLMaker('b152440d8749a910c7225ecf35b548ce')
    url = maker.get_url()
    response = requests.get(url).json()

    # 결과를 저장할 빈 리스트 생성
    result = []
    for movie in response['results']:
        # 평점이 8점을 넘을 경우 result 리스트에 append
        if movie['vote_average'] >= 8:
            result.append(movie)
    return result


if __name__ == '__main__':
    pprint(vote_average_movies())