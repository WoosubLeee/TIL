# Project 02

> 20210129에 진행한 프로젝트입니다.



# 1. problem_a

- `maker = URLMaker('b152440d8749a910c7225ecf35b548ce')`
  - URLMaker 클래스를 생성할 때 TMDB API key값을 추가하여 생성

- `response = requests.get(url).json()`
  - requets.get()으로 url에서 데이터를 전송받고
    .json() 함수를 활용해 딕셔너리로 변환



# 2. problem_b

- problem_a와 같은 방법으로 .json형식의 데이터를 받아 딕셔너리로 변환

- ```
  for movie in response['results']:
      if movie['vote_average'] >= 8:
          result.append(movie)
  ```

  - 각 영화에 대해 vote_average가 8 이상이면 result 리스트에 추가



## 3. problem_c

- problem_a와 같은 방법으로 .json형식의 데이터를 받아 딕셔너리로 변환
- `sorted_movie = sorted(response['results'], key=lambda x: x['vote_average'], reverse=True)`
  - sorted() 함수로 리스트를 정렬하는데
    lambda를 활용해 vote_average 기준으로 정렬시킨다.
    - sorted(iterable, key=lambda x: y) : y value를 기준으로 iterable을 정렬시킨다.
  - reverse=True로 리스트가 내림차순으로 정렬될 수 있도록 변경



## 4. problem_d

- `id = maker.movie_id(title)`

  - id를 얻기 위해 movie_id() 함수를 이용

- ```
  if not id:
          return None
  ```

  - id값이 없을 경우 None을 반환

- `url = maker.get_url(feature=f'{id}/recommendations', region='KR', language='ko')`

  - get_url() 함수를 이용해 url을 구한다.
  - category 인자까지는 동일하고, 
    feature 인자에 f'{id}/recommendations}'을 추가한다.
  - 응답 데이터를 한국어로 받기 위해
    **kwargs 인자로 `region='KR', language='ko'`를 추가한다.



## 5. problem_e

- `url = maker.get_url(feature=f'{id}/credits')`

  - category 인자까지는 동일하고, 
    feature 인자에 f'{id}/credits}'를 추가한다.

- `result = {'cast': [], 'crew': []}`

  - 반환값을 담을 result 딕셔너리를 미리 선언한다.

- ```
  for p in response['cast']:
          if p['cast_id'] < 10:
              result['cast'].append(p['name'])
  ```

  - cast 리스트 중 cast_id의 값이 10 미만인 항목만 result 리스트에 append한다.



## 배운 것 & 느낀 점

1.  lambda 활용법

   - `lambda variable, …: expression`
     - `sorted(iterable, key=lambda x: y)`
       - y value를 기준으로 iterable을 정렬시킨다.

   길게 반복문을 풀어써야 했던 것을 lambda를 이용하면 훨씬 짧게 줄일 수 있었다.

   다만 어느 정도 이해는 했으나 완벽히 이해하지는 못한 것 같다. sorted()를 활용한 방법 이외에도 활용 방법이 무궁무진한 것 같으니 좀 더 공부해 보자.

2. requests 모듈을 활용해 api로부터 데이터를 받는 법.

   이전에는 api라는 것을 알고, requests 모듈을 써야한다는 것을 알아도 활용할 줄을 몰랐는데
   이제는 어떻게 데이터를 받을 수 있을지 확실히 알게 되었다.

3. .env 활용법

   - 라이브러리 내에 .env 파일 생성

   - .env 파일 내에 키값 변수 선언

   - `from decouple import config`

   - ```
     KEY = config('KEY')  # .env 내에서 선언한 변수 이름
     function(key=KEY)
     ```

   제출한 파일에는 없지만 교수님이 가르쳐 주신 .env를 활용한 key값 보호 방법

   API key 값을 보호할 때 유용하게 쓰일 것 같다.(특히, 주식이나 암호화폐 등 자산과 관련된 것)