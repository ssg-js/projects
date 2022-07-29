import requests
from pprint import pprint


def recommendation(title):
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
    # 영화 id로 추천영화 얻기
    recommend = []
    path_recommend = f'/movie/{movie_id}/recommendations'
    response = requests.get(Base_URL + path_recommend, params=params)
    data_recommend = response.json()['results']
    for movie in data_recommend:
        recommend.append(movie['title'])

    return recommend


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 id 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None
