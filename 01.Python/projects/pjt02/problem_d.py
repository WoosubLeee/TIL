import requests
from tmdb import URLMaker
from pprint import pprint


def recommendation(title):
    maker = URLMaker('b152440d8749a910c7225ecf35b548ce')
    id = maker.movie_id(title)
    
    # id값이 없을 경우 None 반환
    if not id:
        return None

    # get_url 함수 실행
    # 추천 영화 리스트를 요청하기 위해 feature 값에 'id/recommendations' 추가
    # 한국어로 응답받기 위해 **kwargs에 region과 language 추가
    url = maker.get_url(feature=f'{id}/recommendations', region='KR', language='ko')
    response = requests.get(url).json()
    result = []
    # 추천 영화 리스트의 제목만 result 리스트에 append
    for i in response['results']:
        result.append(i['title'])
    
    return result


if __name__ == '__main__':
    # 제목 기반 영화 추천
    pprint(recommendation('기생충'))
    # =>   
    # ['원스 어폰 어 타임 인… 할리우드', '조조 래빗', '결혼 이야기', '나이브스 아웃', '1917', 
    # '조커', '아이리시맨', '미드소마', '라이트하우스', '그린 북', 
    # '언컷 젬스', '어스', '더 플랫폼', '블랙클랜스맨', '포드 V 페라리', 
    # '더 페이버릿: 여왕의 여자', '두 교황', '작은 아씨들', '테넷', '브레이킹 배드 무비: 엘 카미노']
    pprint(recommendation('그래비티'))    
    # => []
    pprint(recommendation('id없는 영화'))
    # => None
