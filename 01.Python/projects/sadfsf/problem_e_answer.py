import json


def dec_movies(movies):
    titles = []
    for movie in movies:
        # release_date를 슬라이싱하여 개봉월을 추출한 후 '12'이면 titles list에 title을 추가
        if movie['release_date'][5:7] == '12':
            titles += [movie['title']]
    return titles
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))