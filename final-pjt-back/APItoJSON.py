import requests
import json


all_genre_list = []
all_actor_list = []
all_movie_list = []


BASE_URL = 'https://api.themoviedb.org/3'
API_KEY = '40de101844c75c1524786a8412f97bd3'


ALL_GENRE_PATH = '/genre/movie/list'

genre_response = requests.get(
    BASE_URL + ALL_GENRE_PATH,
    params = {
        'api_key': API_KEY,
        'language': 'ko',
    }    
).json()

genre_list = genre_response.get('genres')

for genre_info in genre_list:
    genre_id = genre_info.get('id')
    genre = {
        'model': 'movies.genre',
        'pk': genre_id,
        'fields': genre_info,
    }
    all_genre_list.append(genre)    

# 출력할 페이지의 갯수 입력
amount_of_page = 10
for page in range(1, 1 + amount_of_page):
    ALL_MOVIE_PATH = '/discover/movie'
    list_response = requests.get(
        BASE_URL + ALL_MOVIE_PATH,
        params = {
            'api_key': API_KEY,
            'language': 'ko',
            'region': 'KR',
            'page': page,
        } 
    ).json()
    movie_list = list_response.get('results')
    
    for index, movie_info in enumerate(movie_list):
        
        date_opened = movie_info.get('release_date')

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
        poster_path = detail_response.get('poster_path')
    
        # if detail_response.get('video') != 'false':
        #     trailer_key = detail_response.get('video')

        genres_info = detail_response.get('genres')

        genres_of_movie = []
        for genre_info in genres_info:
            genre_id = genre_info.get('id')
            genres_of_movie.append(genre_id)
        

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
            all_actor_list.append(actor)


        MOVIE_VIDEO_PATH = '/movie/{}/videos'.format(movie_id)

        video_response = requests.get(
            BASE_URL + MOVIE_VIDEO_PATH,
            params= {
                'api_key': API_KEY,
                'language': 'ko',
            }
        ).json()

        video_list = video_response.get('results')
        for video_info in video_list:
            if not index:
                print(video_info.get('key'))
            if video_info.get('site') == 'YouTube':
                trailer_key = video_info.get('key')


        movie = {
            'model': 'movies.movie',
            # 'pk': page * 20 + index,
            'pk': movie_id,
            'fields': {
                'id': movie_id,
                'movie_title': movie_title,
                'date_opened': date_opened,
                'overview': overview,
                'trailer_key': trailer_key,
                'poster_path': poster_path,
                'starring': starring,
                'genres_of_movie': genres_of_movie,
            }
        }
        
        all_movie_list.append(movie)


with open('./movies/fixtures/genres.json', 'w', encoding='UTF-8') as outfile:
    json.dump(all_genre_list, outfile, indent=4, ensure_ascii=False)
with open('./movies/fixtures/actors.json', 'w', encoding='UTF-8') as outfile:
    json.dump(all_actor_list, outfile, indent=4, ensure_ascii=False)
with open('./movies/fixtures/movies.json', 'w', encoding='UTF-8') as outfile:
    json.dump(all_movie_list, outfile, indent=4, ensure_ascii=False)
