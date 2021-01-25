import json


def title_length(movie):
    # len함수를 사용해 movie['title']의 길이를 반환한다.
    return len(movie['title'])


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('problem02_data.json', encoding='UTF8')
    movie = json.load(movie_json)
    print(title_length(movie)) 
    # => 4