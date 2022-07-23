import json


def nineties_revenue_movies(movies):
    movies_revenue = {}  # 90년대 개봉작의 수입와 이름
    for movie in movies:
        movie_id = movie.get("id")  # 영화의 id -> 파일명
        file_json = open('data/movies/' + str(movie_id) + '.json', encoding='utf-8')
        info_file = json.load(file_json)  # info_file : {}, 각 영화의 정보
        release_year = info_file.get("release_date")[:3]
        if release_year == '199':  # 199x년 개봉 영화
            movies_revenue[info_file.get("title")] = info_file.get("revenue")
            movie_rank = sorted(movies_revenue)  # 90년대 개봉작 중 수입에 따른 순위
            # movie_revenue.items()로 sorted하면 수입도 같이 저장됨
    return movie_rank


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)

    print(nineties_revenue_movies(movies_list))
