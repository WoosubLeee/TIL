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
