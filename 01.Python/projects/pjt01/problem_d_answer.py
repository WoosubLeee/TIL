import json


def max_revenue(movies):
    max_revenue = 0
    max_title = ''
    for movie in movies:
        # id를 이용, movies 폴더에서 id에 맞는 영화의 정보를 load
        id = movie['id']
        info = json.load(open(f'data/movies/{id}.json', encoding='UTF8'))

        # 'revenue'를 구하고 그 값이 이전까지 구한 max_revenue보다 크면 max_revenue 값과 그 값을 가진 영화를 교체
        revenue = info['revenue']
        if revenue > max_revenue:
            max_revenue = revenue
            max_title = info['title']

    return max_title
        
 
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))