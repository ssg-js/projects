# 02_pjt

## A. 인기 영화 조회

### 문제

- requests 라이브러리를 사용하여 TMDB에서 현재 인기있는 영화 목록(Get Popalar) 데이터를 요청하여 응답 받은 데이터의 영화 개수를 반환하는 함수 popular_count를 작성합니다.

### 풀이

```python
def popular_count():
    # API로 데이터 받아오기
    Base_URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
        'api_key': 'd1d99f07a889e254f0bdcbf18c0530bb',
    }
    response = requests.get(Base_URL + path, params=params)
    data = response.json()
    count = len(data['results'])

    return count
```

### 어려웠던 점 및 해결 방법

API로 받은 Json 파일이 어떤 구조인지를 몰라서 영화들에 대한 정보가 'results' 키에 연결된 리스트 안에 딕셔너리 형태로 있다는 사실을 몰랐습니다. 그래서 출력을 해보고 나서 알았습니다.

## B. 특정 조건에 맞는 인기 영화 조회 1

### 문제

- TMDB에서 현재 인기있는 영화 목록(Get Popular) 데이터를 요청해서 응답 받은 데이터 중 평점(vot_average)이 8점 이상인 영화 목록을 반환하는 함수 vot_average_movies를 작성합니다.

### 풀이

```python
def vote_average_movies():
    # API로 데이터 받아오기
    Base_URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
        'api_key': 'd1d99f07a889e254f0bdcbf18c0530bb',
    }
    response = requests.get(Base_URL + path, params=params)
    data = response.json()
    popular_movie = []
    for movie in data['results']:  # 영화들 중에 평점이 8이상인 영화를 추출
        if movie['vote_average'] >= 8:
            popular_movie.append(movie)

    return popular_movie
```

### 어려웠던 점 및 해결 방법

- A 문제랑 비슷해서 무리없이 풀 수 있었습니다.

## C. 특정 조건에 맞는 인기 영화 조회 2

### 문제

- TMDB에서 현재 인기있는 영화 목록(Get Popular) 데이터를 요청하여 응답 받은 데이터 중 평점(vote_average)을 기준으로 평점이 높은 영화 5개 정보를 리스트로 반환하는 함수 ranking을 작성합니다.

- sort 메서드 혹은 sorted 함수의 특정 파라미터를 이용합니다.

### 해결

```python
def ranking():
    Base_URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
        'api_key': 'd1d99f07a889e254f0bdcbf18c0530bb',
    }
    response = requests.get(Base_URL + path, params=params)
    data = response.json()
    popular_movies = sorted(
        data['results'], key=lambda x: x['vote_average'], reverse=True
    )

    return popular_movies[:5]
```

### 어려웠던 점 및 해결방법

- 정렬을 하기 위해서 해당 자료('vote_average')에 접근해야 하는데 어떻게 접근해야 할지 헷갈렸습니다. 그래서 방법을 찾던 중 lambda 함수를 이용하여 sorted() 함수의 key값을 주는 것으로 해결했습니다.

## D. 특정 추천 영화 조회

### 문제

- 제공된 영화 제목으로 TMDB에서 영화를 검색(Search Movies)해서 응답 받은 결과 중 첫번째 영화의 id 값을 찾아 해당 영화에 대한 추천 영화 목록(Get Recommendations)을 출력하는 recommendation을 작성합니다.

### 풀이

```python
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
```

### 어려웠던 점 및 해결방법

- 어려가지 형태의 자료들을 받다 보니깐 어떤 구조로 이뤄져있는지 일일히 확인하기 어려웠습니다. 그런데 TMDB 사이트의  api 사용설명에 어떤 구조로 이뤄져있는지를 확인할 수 있었습니다. 앞의 문제들을 풀 때 지나쳤던 부분이었습니다. 

- Query 값이 어떤 역할을 하는지 모르고 그냥 설명란에 있던 String 을 복사해서 붙여넣었었는데 출력값을 확인해보니 다 string이 들어간 영화가 나와서 그때 영화 제목을 넣어야 한다는 것을 알았습니다. 설명란에 자세히 보면  search할 영화제목을 넣어라고 되어있었습니다. 앞으로 문서를 꼼꼼히 봐야겠습니다.

## E. 출연진, 연출진 데이터 조회

## 1. 풀이

- 제공된 영화 제목으로 TMDB에서 영화를 검색(Search Movies)해서 응답 받은 결과 중 첫번째 영화의 id 값을 찾아 해당 영화에 대한 출연진과 스태프 목록(Get Credits)을 가져옵니다.

- 출연진은 cast_id 값이 10 미만인 출연진만 추출하며, 연출진은 스태프 부서가 Directing인 데이터만 추출하여 반환하는 함수 credits를 작성합니다.

```python
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
```

### 어려웠던 점 및 해결 방법

- 앞의 문제에서 자료가 추가적으로 들고오는 거라 큰 문제 없이 풀었습니다.



## 배운 점 및 느낀 점

- API를 통해 json파일을 받아 자료를 처리하는 방법

- sorted 함수의 key 사용법과 lambda 함수의 사용법

- 리스트와 딕셔너리가 복잡하게 얽힌 자료형을 당황하지 않고 처리하는 방법

- API를 통해 이렇게 자료를 불어오는게 정말 낯설었는데 오늘 프로젝트를 통해 생각보다 간단하다는 느낌을 받았습니다. 

- 그리고 알고리즘을 대충 머리고 짜고 코딩을 하는데 그러다 보니 중간에 맞지 않는 알고리즘이 많이 쌓이다 보니깐 제 코딩에 제가 헷갈려서 힘들었던 점이 많았습니다. 앞으로 그렇게 조금 대충 짜는 버릇을 좀 고치고 처음부터 논리적으로 잘 생각하고 코딩을 해야겠다고 생각했습니다.

- 그리고 탑건 메버릭 제목을 많이 보다 보니깐 안봤던 영화인데 넘 보고싶어서 영화관을 가야겠다고 생각했습니다.
