# Project 01

> 20210122에 진행한 프로젝트입니다.



## 1. problem_a

```
def movie_info(movie):
    result = {}
    # for문을 활용하여 각 key에 해당하는 value를 구해 result에 추가
    for info in ['id', 'title', 'poster_path', 'vote_average', 'overview', 'genre_ids']:
        result[info] = movie[info]

    return result
```

for문을 활용하여 각 key에 해당하는 value를 구하여 result 딕셔너리에 추가합니다.

key마다 각각 코드를 작성하기보다 반복문을 사용하여 코드를 줄이고자 하였습니다.



## 2. problem_b

```
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
```

problem_a와 같은 코드로 영화에 대한 정보를 구한 후 이중 for문을 활용

1단계 : 영화의 각 'genre_id'에 대해
2단계 : genres의 장르들을 차례대로 조회하여 'genre_id'에 맞는 장르를 찾아냅니다.

infos에서 'genre_ids'가 'genre_names'로 교체되어야 하므로
result 딕셔너리를 새로 만들어 'genre_names'와 'names' 리스트를 추가 후
'infos'에서 'genre_ids'를 제외한 정보들을 result에 추가합니다.



## 3. problem_c

```
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
```

for문을 활용, movies내의 각각의 영화들에 대해 problem_b까지의 코드로 조회합니다.

한 영화의 정보는 일단 result_a_movie에 담고
그 후 모든 영화의 정보를 담은 result_movies 리스트와 합치게 됩니다.



## 4. problem_d

```
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
```

함수가 실행될 때, 가장 높은 수익을 담을 max_revenue와 그 수익을 낸 영화를 담을 max_title 변수를 initialize합니다.

for문을 활용, movies 내의 각각의 영화들의 id를 이용하여 상세정보를 조회하였습니다.

그 후 revenue를 구하고 만약 그 값이 기존의 max_revenue보다 크다면
max_revenue를 새 revenue로 교체하고
max_title도 해당 revenue를 낸 영화의 title로 교체합니다.



## 5. problem_e

```
def dec_movies(movies):
    titles = []
    for movie in movies:
        # release_date를 슬라이싱하여 개봉월을 추출한 후 '12'이면 titles list에 title을 추가
        if movie['release_date'][5:7] == '12':
            titles += [movie['title']]
    return titles
```

release_date에서 개봉월을 추출하는 방법으로는

1. datetime을 활용
2. 슬라이싱

을 찾았습니다. 이 중 string 슬라이싱하는 방법을 활용하였습니다.

추출한 개봉월이 '12'와 같으면 titles 리스트에 해당 영화의 title이 추가됩니다.



## * 느낀 점

1. 큰 어려움은 없었으나 problem_b를 풀며 list와 dictionary 구조 사이에 혼동하여 정체됐었다. 머릿속에서 구조화 시킬 수 있는 연습이 필요할 것 같다.
2. 주석과 markdown 작성하는 것이 쉽지 않았다. 처음 읽는 사람도 내용을 잘 이해할 수 있도록 작성하는 것이 어려웠다.
3. variable 이름을 좀 더 잘 짓고 싶다. 너무 길지 않으면서 그 variable이 담고 있는 내용을 파악하기 쉬운 그런 이름... 그런 name...