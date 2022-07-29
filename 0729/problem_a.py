import requests


def popular_count():
    Base_URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
        'api_key': 'd1d99f07a889e254f0bdcbf18c0530bb',
    }
    response = requests.get(Base_URL + path, params=params)
    data = response.json()
    count = len(data['results'])

    return count


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
