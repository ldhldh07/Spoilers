import requests

all_movie_list = []

for page in range(1, 3):
    BASE_URL = 'https://api.themoviedb.org/3'
    ALL_MOVIE_PATH = '/discover/movie'
    response = requests.get(
        BASE_URL + ALL_MOVIE_PATH,
        params = {
            'api_key' : '40de101844c75c1524786a8412f97bd3',
            'language' : 'ko',
            'region' : 'KR',
            'page' : page
        } 
    ).json()

    movie_list = response.get('results')
    for index, movie_info in enumerate(movie_list):
        movie_id = movie_info.get('id')
        MOVIE_DETAIL_PATH = '/movie/{}'.format(movie_id)

        response = requests.get(
            BASE_URL + MOVIE_DETAIL_PATH,
            params = {
                'api_key' : '40de101844c75c1524786a8412f97bd3',
                'language' : 'ko',
            } 
        ).json()

        movie = {
            'model': 'movies.movie',
            'pk': page * 20 + index,
            'fields': {
                
            }
        }

    # movie_list

print(len(movie_list))