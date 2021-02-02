import json
from pprint import pprint


def movie_info(movie):
    result = {}
    # for문을 활용하여 각 key에 해당하는 value를 구해 result에 추가
    for info in ['id', 'title', 'poster_path', 'vote_average', 'overview', 'genre_ids']:
        result[info] = movie[info]

    return result


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie_dict = json.load(movie_json)
    
    pprint(movie_info(movie_dict))