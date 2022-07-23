# 01_pjt

## A. 제공되는 영화 데이터의 주요내용 수집

#### 문제

- 샘플 영화 데이터(movie.json)를 이용하여 id, title, poster_path, vote_average, overview, genro_ids 키에 해당하는 값을 추출합니다.
- 추출한 값을 새로운 dictionary로 반환하는 함수 movie_info를 완성합니다.

#### 풀이

```python
def movie_info(movie):
    info = {
        "id": movie.get("id"),
        "title": movie.get("title"),
        "poster_path": movie.get("poster_path"),
        "vote_average": movie.get("vote_average"),
        "overview": movie.get("overview"),
        "genre_ids": movie.get("genre_ids"),
    }

    return info
```

#### 어려웠던 점

- 처음 사용하는 get() 함수의 사용법이 어색했습니다.

#### 해결 방법

- 주어진 example들로 사용법을 익힌 후 코딩을 시작했습니다.

## B. 제공되는 영화 데이터의 주요내용 수정

#### 문제

- 샘플 영화 데이터(movie.json)를 이용하여 id, title, poster_path, vote_average, overview, genro_ids 키에 해당하는 값을 추출합니다.

- genres.json을 이용하여 genre_ids를 각 장르 번호에 맞는 name 값으로
  대체한 genre_names 키를 생성합니다.

- 위 요구사항을 반영한 새로운 dictionary를 반환하는 함수 movie_info를
  완성합니다.

#### 풀이

```python
def movie_info(movie, genres):
    genre_name = list()  # 해당 영화의 장르들을 저장하는 리스트
    for genre in genres:
        for genre_id in movie.get("genre_ids"):
            if genre["id"] == genre_id:
                genre_name.append(genre["name"])

    info = {
        "id": movie.get("id"),
        "title": movie.get("title"),
        "poster_path": movie.get("poster_path"),
        "vote_average": movie.get("vote_average"),
        "overview": movie.get("overview"),
        "genre_names": genre_name,
    }

    return info
```

#### 어려웠던 점

- 튜플형태의 movie와 튜플이 원소로 들어가있는 리스트인 genre_list의 차이때문에 많이 혼동했습니다.

- movie.json에서 받아온 genro_ids를 각 장르 번호에 맞는 name으로 불러오는 for문을 작성할 때 해당 영화의 장르들을 저장하는 리스트의 선언과 초기화를 어디에 할지 어려움을 느꼈습니다.

- 결과가 계속 아예 다르게 출력이 되었습니다.

#### 해결 방법

- 주석을 붙였습니다.

- 아예 다르게 나온 이유는 당연히 잘못 코딩했을 거라고 생각한 for문 안에서가 아닌 return 값을 잘못 줘서였다는 것을 발견했습니다.

## C. 다중 데이터 분석 및 수정

#### 문제

- 여러 개의 영화의 정보를 담고 있는 movies.json을 활용합니다.

- 개별 영화 데이터는 id, title, poster_path, vote_average, overview, 
  genre_names 키와 이에 해당하는 값을 가집니다.

- 위 요구사항을 반영한 새로운 list를 반환하는 함수 movie_info를 완성합니다.

#### 풀이

```python
def movie_info(movies, genres):
    infos = list()  # 영화들의 정보들를 저장하는 리스트
    for movie in movies:
        genre_name = list()  # 해당 영화의 장르들을 저장하는 리스트
        for genre in genres:
            for genre_id in movie.get("genre_ids"):
                if genre["id"] == genre_id:
                    genre_name.append(genre["name"])

        infos.append(
            {
                "id": movie.get("id"),
                "title": movie.get("title"),
                "poster_path": movie.get("poster_path"),
                "vote_average": movie.get("vote_average"),
                "overview": movie.get("overview"),
                "genre_names": genre_name,
            }
        )

    return infos
```

#### 어려웠던 점

- 처리해야 하는 변수의 형태가 다양해져서 for문을 사용할 때 값들을 저장할 변수(infos)의 선언과 초기화를 어디에 할지 어려움을 느꼈습니다.

#### 해결 방법

- 주석을 붙이고 코드를 좀 더 가독성 좋게 적어보았습니다.

## D. 알고리즘을 사용한 데이터 출력

#### 문제

- movies 폴더 내부의 영화의 추가 정보를 이용하여 가장 높은 수익을 낸 영화의 제목을 출력하는 함수 max_revenue를 완성합니다.

#### 풀이

```python
def max_revenue(movies):
    max = 0  # 영화수입(revenue) 최대값을 저장
    for movie in movies:
        movie_id = movie.get("id")  # 영화의 id -> 파일명
        file_json = open('data/movies/' + str(movie_id) + '.json', encoding='utf-8')
        info_file = json.load(file_json)  # info_file : {}, 각 영화의 정보
        revenue = info_file.get("revenue")
        if max < revenue:
            max = revenue
            max_title = info_file.get("title")
    return max_title
```

#### 어려웠던 점

- 파일을 오픈할 때 해당 파일을 불어오는 argument를 어떻게 줘야 하는지 고민했습니다.

#### 해결 방법

- argument가 string인 것을 보고 '+' 연산자로 해당 폴더의 파일을 불러올 수 있도록 했습니다.

## E. 알고리즘을 사용한 데이터 출력

#### 문제

- movies 폴더 내부의 정보 중 개봉일 정보(release_date)를 이용하여 모든 영화 중 12월에 개봉한 영화들의 제목을 리스트로 출력하는 함수 dec_movies를 완성합니다.

#### 풀이

```python
def dec_movies(movies):
    month_movies = list()  # 12월 개봉한 영화들을 모아둘 list
    for movie in movies:
        movie_id = movie.get("id")  # 영화의 id -> 파일명
        file_json = open('data/movies/' + str(movie_id) + '.json', encoding='utf-8')
        info_file = json.load(file_json)  # info_file : {}, 각 영화의 정보
        release_month = info_file.get("release_date")[5:7]
        if release_month == '12':
            month_movies.append(info_file.get("title"))
    return month_movies
```

#### 어려웠던 점

- 아무래도 사용하는 자료가 많아지다 보니깐 변수의 개수가 많아져서 사용하는 데 혼동해서 사용하였습니다. 그래서 run 했을 때 출력이 잘못 나와도 어디 잘못 나온 것인지 찾지를 못했습니다.

- release_date가 string 형태로 '0000-00-00' 이렇게 되어있었는데 어떻게 월(month)에 해당하는 부분만 가져올지 고민했습니다.

#### 해결 방법

- 원래 a,b 등 단순한 변수명만을 사용했었는데 변수가 담고있는 자료를 나타내는 변수명을 사용하면서 혼동하는 일이 줄었습니다. 

- 처음에는 datetime모듈에 대해서 알아봤는데 import를 해야 사용할 수 있어서, 다른 방법을 찾았습니다. 그 다음으로 생각한 방법인 slicing을 문제를 해결하였습니다.

## 프로젝트 소감

#### 배운 점

- 주석을 많이 달수록 코드의 이해에 도움이 된다는 사실

- get() 함수의 사용법

- .json 파일 오픈해서 안의 자료들을 처리하는 방법

- 변수명의 중요성

#### 느낀 점

- 기본이 정말 중요하다는 생각이 들었습니다. 주석과 변수명은 정말 초반에 배운 내용인데 코드 줄의 개수가 조금만 늘어서 기본으로 배운 내용이 빛을 발한다는 사실을 느꼈습니다. 그리고 실습이 정말 중요하다는 생각이 들었습니다. 수업을 들었으니깐 알고 있을 거라고 생각했는데 막상 코딩을 해보니 헷갈리는 부분이 많았습니다. 처음에는 오늘 다 할 수 있을까 걱정했는데 완료할 수 있어서 다행이고 뿌듯합니다.
