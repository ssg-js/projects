import json


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


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)

    print(max_revenue(movies_list))
