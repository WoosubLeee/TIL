# Project 08

> 20210430에 진행한 프로젝트입니다.



### Serializer

```python
# movies/serializers.py

from rest_framework import serializers
from .models import Movie, Review, Comment

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('review',)


class ReviewSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('movie',)


class MovieSerializer(serializers.ModelSerializer):
    review_set = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'
        

class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('id', 'title', 'overview',)
```

DRF에서 제공하는 ModelSerializer를 이용해 serializer를 만든다.

- `read_only_fields = ('review',)` : 참조받는 모델은 따로 입력하지 않도록 하기 위해 설정
- `comment_set = CommentSerializer(many=True, read_only=True)` : 1:N 관계로 참조하고 있는 인스턴스를 자동으로 불러온다.
  - https://www.django-rest-framework.org/api-guide/relations/#nested-relationships

```python
# movies/urls.py

urlpatterns = [
    path('movies/', views.movie_list),
    path('movies/<int:movie_pk>/', views.movie_detail),
    path('movies/<int:movie_pk>/reviews/', views.review_create),
    path('movies/<int:movie_pk>/reviews/<int:review_pk>/', views.review_detail),
    path('movies/<int:movie_pk>/reviews/<int:review_pk>/comments/', views.comment_create),
    path('movies/<int:movie_pk>/reviews/<int:review_pk>/comments/<int:comment_pk>', views.comment_detail),
]
```

### 영화 정보 조회

```python
# movies/views.py

@api_view(['GET'])
def movie_list(request):
    movies = get_list_or_404(Movie)
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)
```

### 리뷰 생성

```python
# movies/views.py

@api_view(['POST'])
def review_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
```

### 리뷰 정보 조회

```python
# movies/views.py

@api_view(['GET', 'PUT', 'DELETE'])
def review_detail(request, movie_pk, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        review.delete()
        data = {
            '{}번 리뷰가 삭제되었습니다'.format(review_pk)
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)
```

### 댓글 생성

```python
# movies/views.py

@api_view(['POST'])
def comment_create(request, movie_pk, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(review=review)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
```

### 댓글 정보 조회

```python
# movies/views.py

@api_view(['GET'])
def comment_detail(request, movie_pk, review_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    serializer = CommentSerializer(comment)
    return Response(serializer.data)
```

### TMDB로부터 데이터 받아오기

```python
# movies/get_api.py

import json
import requests
from pprint import pprint


class URLMaker:

    def __init__(self, key):
        self.key = key


    def get_url(self, category='movie', feature='popular', **kwargs):
        url = f'https://api.themoviedb.org/3/{category}/{feature}'
        url += f'?api_key={self.key}'

        for k, v in kwargs.items():
            url += f'&{k}={v}'

        return url


def make_data(movies):
    data = []
    for idx, movie in enumerate(movies['results']):
        movie_data = {'model': 'movies.movie', 'pk': idx+1, 'fields': {}}
        for i in ['title', 'overview', 'poster_path', 'release_date']:
            movie_data['fields'][i] = movie[i]
        data.append(movie_data)
    
    with open('movies/fixtures/movies/movies.json', 'w', encoding='utf-8') as make_file:
        json.dump(data, make_file, indent="\t")


url_maker = URLMaker('b152440d8749a910c7225ecf35b548ce')
url = url_maker.get_url()
response = requests.get(url).json()
make_data(response)

```

- `class URLMaker` : api key값을 인자로 받아 요청을 보낼 url을 생성한다.
- `make_data` : 생성한 모델에 맞춰 응답받은 json 데이터를 가공한다.



### Point

- 기존에 하던 웹페이지 만드는 것이 아니라 api를 구성하는 것이어서 처음에 어려웠다
- api로부터 응답받은 데이터를 바로 db에 저장하려 시도해보았으나 쉽지 않았다