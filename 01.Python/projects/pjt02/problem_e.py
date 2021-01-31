import requests
from tmdb import URLMaker
from pprint import pprint


def credits(title):
    maker = URLMaker('b152440d8749a910c7225ecf35b548ce')
    id = maker.movie_id(title)

    if not id:
        return None
    
    # 영화 크레딧 리스트를 요청하기 위해 feature에 'id/credits' 추가
    url = maker.get_url(feature=f'{id}/credits')
    response = requests.get(url).json()

    result = {'cast': [], 'crew': []}
    # cast 리스트 중 cast_id 값이 10 미만인 사람만 result에 append
    for p in response['cast']:
        if p['cast_id'] < 10:
            result['cast'].append(p['name'])
    # crew 리스트 중 Directing department인 사람만 result에 append
    for p in response['crew']:
        if p['known_for_department'] == 'Directing':
            result['crew'].append(p['name'])
    return result


if __name__ == '__main__':
    # id 기준 주연배우 감독 출력
    pprint(credits('기생충'))
    # => 
    # {
    #     'cast': [
    #         'Song Kang-ho',
    #         'Lee Sun-kyun',
    #         'Cho Yeo-jeong',
    #         'Choi Woo-shik',
    #         'Park So-dam',
    #         'Lee Jung-eun',
    #         'Chang Hyae-jin'
    #     ],
    #      'crew': [
    #         'Bong Joon-ho',
    #         'Han Jin-won',
    #         'Kim Seong-sik',
    #         'Lee Jung-hoon',
    #         'Park Hyun-cheol',
    #         'Yoon Young-woo'
    #     ]
    # } 
    pprint(credits('id없는 영화'))
    # => None