import json


def over(movie):
    # user_rating이 8 이상이라면 True를 반환하고, 미만이라면 False를 반환한다.
    return movie['user_rating'] >= 8


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('problem02_data.json', encoding='UTF8')
    movie = json.load(movie_json)
    print(over(movie)) 
    # => True