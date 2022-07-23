import json
from pprint import pprint


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


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='utf-8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))
