import json
from pprint import pprint


def movie_info(movies, genres):
    # for문을 활용하여 movies 내의 모든 영화들에 대해 조회
    result_movies = []
    for movie in movies:
        # for문을 활용하여 각 키에 해당하는 정보를 구해 infos에 추가
        infos = {}
        for info in ['id', 'title', 'poster_path', 'vote_average', 'overview', 'genre_ids']:
            infos[info] = movie[info]

        # 이중 for문(1단 : 각 id에 대해, 2단 : id에 맞는 장르 찾기)을 활용해 genres에서 장르 name 찾기
        names = []
        for id in infos['genre_ids']:
            for genre in genres:
                if genre['id'] == id:
                    names += [genre['name']]
        
        # result_a_movie에 장르 name을 추가하고 나머지 정보들을 추가
        result_a_movie = {}
        result_a_movie['genre_names'] = names
        for info in ['id', 'title', 'poster_path', 'vote_average', 'overview']:
            result_a_movie[info] = infos[info]
        # result_movies에 기존 정보와 result_a_movie의 정보를 합침
        result_movies += [result_a_movie]

    return result_movies

        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))