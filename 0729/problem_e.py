import requests
from pprint import pprint


def credits(title):
    # 검색후 첫번째 영화 id 얻기
    Base_URL = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    params = {
        'api_key': 'd1d99f07a889e254f0bdcbf18c0530bb',
        'query': title,  # 검색할 영화 제목
    }
    response = requests.get(Base_URL + path, params=params)
    data = response.json()['results']  # 영화 데이터들 불러오기
    if not data:
        return None
    movie_info = data[0]
    movie_id = movie_info['id']
    # id로 출연진과 스태프 목록 가져오기
    path_credits = '/movie/' + str(movie_id) + '/credits'
    response = requests.get(Base_URL + path_credits, params=params)
    cast_members = response.json()['cast']  # cast 에 있는 배우들만
    cast = []
    for member in cast_members:
        if member['cast_id'] < 10:
            cast.append(member['name'])
    crew_members = response.json()['crew']  # crew 에서 Directing 부서만
    directing = []
    for member in crew_members:
        if member['department'] == 'Directing':
            directing.append(member['name'])

    credit_members = {
        'cast': cast,
        'directing': directing,
    }

    return credit_members


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
