import requests
import json
import sys

BASE_URL = 'https://api.themoviedb.org/3'
API_KEY = '40de101844c75c1524786a8412f97bd3'

# 상대 위치이기 때문에 final-pjt-back 위치에서 실행할것
# 장르 리스트 파일 로드
# 시간이 좀 걸리더라도 중복 검사를 위해 로드해서 다시 파일화
with open('./movies/fixtures/genres.json', 'r', encoding='UTF-8') as file:
    all_genre_list = json.load(file)

# 장르 데이터 API 요청
ALL_GENRE_PATH = '/genre/movie/list'

genre_response = requests.get(
    BASE_URL + ALL_GENRE_PATH,
    params = {
        'api_key': API_KEY,
        'language': 'ko',
    }    
).json()

genre_list = genre_response.get('genres')

# 개별 데이터 Parsing해서 리스트 담기
for genre_info in genre_list:
    genre_id = genre_info.get('id')
    genre = {
        'model': 'movies.genre',
        'pk': genre_id,
        'fields': genre_info,
    }
    if genre not in all_genre_list:
        all_genre_list.append(genre)    

# 장르 데이터 파일 출력
with open('./movies/fixtures/genres.json', 'w', encoding='UTF-8') as outfile:
    json.dump(all_genre_list, outfile, indent=4, ensure_ascii=False)


# 영화 데이터 API 요청

# 요청할 페이지
starting_page = 341
amount_of_page = 10
for page in range(starting_page, starting_page + amount_of_page):
    ALL_MOVIE_PATH = '/discover/movie'
    list_response = requests.get(
        BASE_URL + ALL_MOVIE_PATH,
        params = {
            'api_key': API_KEY,
            'language': 'ko',
            'region': 'KR',
            'sort_by': 'popularity.desc',
            'page': page,
        } 
    ).json()
    movie_list = list_response.get('results')
    
    for index, movie_info in enumerate(movie_list):
                
        # 현재 json데이터 파일 로드
        with open('./movies/fixtures/actors.json', 'r', encoding='UTF-8') as file:
            all_actor_list = json.load(file)
        with open('./movies/fixtures/movies.json', 'r', encoding='UTF-8') as file:
            all_movie_list = json.load(file)

        date_opened = movie_info.get('release_date')

        # 개별 영화 정보 담긴 API 요청
        movie_id = movie_info.get('id')
        MOVIE_DETAIL_PATH = '/movie/{}'.format(movie_id)

        detail_response = requests.get(
            BASE_URL + MOVIE_DETAIL_PATH,
            params = {
                'api_key': API_KEY,
                'language': 'ko',
            } 
        ).json()
        movie_title = detail_response.get('title')
        overview = detail_response.get('overview')
        popularity = detail_response.get('popularity')
        poster_path = detail_response.get('poster_path')
        genre_list = detail_response.get('genres')

        genres_of_movie = []
        for genre_info in genre_list:
            genre_id = genre_info.get('id')
            genres_of_movie.append(genre_id)
        
        # 개별 영화 출연진 담긴 API 요청
        MOVIE_CREDITS_PATH = '/movie/{}/credits'.format(movie_id)

        credits_response = requests.get(
            BASE_URL + MOVIE_CREDITS_PATH,
            params = {
                'api_key': API_KEY,
                'language': 'ko',
            } 
        ).json()
        
        starring = []
        casts = credits_response.get('cast')

        # 외래키인 배우 정보는 개별 영화 데이터에 담는 동시에 전체 리스트에도 담음
        for actor_info in casts:
            actor_id = actor_info.get('id')
            actor_name = actor_info.get('name')
            starring.append(actor_id)
            actor = {
                'model': 'movies.actor',
                'pk': actor_id,
                'fields': {
                    'id': actor_id,
                    'name': actor_name,
                }
            }
            if actor not in all_actor_list:
                all_actor_list.append(actor)

        # 배우 리스트는 파일로 출력
        with open('./movies/fixtures/actors.json', 'w', encoding='UTF-8') as outfile:
            json.dump(all_actor_list, outfile, indent=4, ensure_ascii=False)

        # VIDEO API 요청
        MOVIE_VIDEO_PATH = '/movie/{}/videos'.format(movie_id)

        video_ko_response = requests.get(
            BASE_URL + MOVIE_VIDEO_PATH,
            params= {
                'api_key': API_KEY,
                'language': 'ko',
            }
        ).json()
        
        # 트레일러 키 재입력되지 않도록 초기화
        trailer_key = ''
        video_ko_list = video_ko_response.get('results')

        if video_ko_list:
            for video_ko_info in video_ko_list:
                if video_ko_info.get('site') == 'YouTube':
                    trailer_key = video_ko_info.get('key')
        else:
            video_en_response = requests.get(
                BASE_URL + MOVIE_VIDEO_PATH,
                params= {
                    'api_key': API_KEY,
                    'language': 'en',
                }
            ).json()
            video_en_list = video_en_response.get('results')
            for video_en_info in video_en_list:
                if video_en_info.get('site') == 'YouTube':
                    trailer_key = video_en_info.get('key')


        # 전체 영화, 개별 영화, casts, video API 요청해서 얻어온 데이터들 object화 해서 전체 리스트 담기
        movie = {
            'model': 'movies.movie',
            # 'pk': page * 20 + index,
            'pk': movie_id,
            'fields': {
                'id': movie_id,
                'movie_title': movie_title,
                'date_opened': date_opened,
                'overview': overview,
                'popularity': popularity,
                'trailer_key': trailer_key,
                'poster_path': poster_path,
                'starring': starring,
                'genres_of_movie': genres_of_movie,
            }
        }
        if movie not in all_movie_list:
            all_movie_list.append(movie)
            is_new = True
        else:
            is_new = False

        with open('./movies/fixtures/movies.json', 'w', encoding='UTF-8') as outfile:
            json.dump(all_movie_list, outfile, indent=4, ensure_ascii=False)

        if is_new:
            print(f'{page * 20 + index}번째 영화 {movie_title} 데이터 입력 완료')
        else:
            print(f'{page * 20 + index}번째 영화 {movie_title}는(은) 이미 입력되어 있습니다.')

    print(f'{page}페이지 데이터 입력 완료')


    with open('./last_input_page.txt', 'a') as pagetxt:
        pagetxt.write(f'{page}p ')
        pagetxt.write('')