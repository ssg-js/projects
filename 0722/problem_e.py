import json


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


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)

    print(dec_movies(movies_list))
