import json


def history(movie):
    # '과거' string이 movie['overview'] 속에 포함되는지 확인하고 그 값을 반환한다.
    if '과거' in movie['overview']:
        return True
    else:
        return False


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('problem02_data.json', encoding='UTF8')
    movie = json.load(movie_json)
    print(history(movie)) 
    # => False