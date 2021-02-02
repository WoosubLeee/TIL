import json
from pprint import pprint


def movie_info(movie, genres):
    # for문을 활용하여 각 키에 해당하는 정보를 구해 infos에 추가
    infos = {}
    for info in ['id', 'title', 'poster_path', 'vote_average', 'overview', 'genre_ids']:
        infos[info] = movie[info]

    # 이중 for문(1단 : 각 id에 대해, 2단 : id에 맞는 장르 찾기)을 활용해 genres에서 장르 name 찾기
    names = []
    for id in infos['genre_ids']:  # 1단
        for genre in genres:  # 2단
            if genre['id'] == id:
                names += [genre['name']]
    
    # result에 장르 name을 추가하고 나머지 정보들을 추가
    result = {}
    result['genre_names'] = names
    for info in ['id', 'title', 'poster_path', 'vote_average', 'overview']:
        result[info] = infos[info]
    return result


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))