from django.shortcuts import render
from .models import MovieModel, ClipModel
from .recommender.movie_recommender import MovieRecommender
from django.contrib.auth.decorators import login_required

import requests
from bs4 import BeautifulSoup
import random

# Create your views here.
@login_required
def recommend_movies(request):
    if request.method == 'GET':
        mr = MovieRecommender()
        similar = mr.get_similar_movies_on_ibcf('161967', 12)
        similar_recommend = MovieRecommender().get_similar_movies_on_lfcf('161967', 12)
        similar_genre_code = MovieRecommender().get_movies_on_same_genre('93728', 12)
        similar_code = []
        similar_recommend_code = []
        for i in similar:
            similar_code.append(str(i))
        for i in range(12):
            similar_recommend_code.append(str(similar_recommend[i][1]))

        print(similar_genre_code)
        main_movie_clip = get_main_movie_clip()
        return render(request, 'main_page/main_page.html', {'similar_code': similar_code, 'similar_recommend_code':similar_recommend_code,
                                                            'similar_genre_code':similar_genre_code, 'main_movie_clip':main_movie_clip})


# 영화 클립 url을 돌려준다
def get_movie_clip_url(movie_code, multimedia_id):
    url = f"https://movie.naver.com/movie/bi/mi/mediaView.naver?code={movie_code}&mid={multimedia_id}"
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    core_url = soup.select_one('.video_ar iframe')['src']
    full_url = f"https://movie.naver.com{core_url}"
    return full_url


# 영화 정보를 돌려준다(영화id, clip url, 제목, 줄거리)
def get_main_movie_clip():
    movie_id  = [194204,177366,93756,167651,85579,102875,115977,78726]
    draw_movie_id = movie_id[random.randrange(8)]
    clip = ClipModel.objects.filter(movie_id=draw_movie_id).values()[0]
    movie = MovieModel.objects.filter(movie_id=draw_movie_id).values()[0]
    if clip['video_url'] == 'None':
        video_url = get_movie_clip_url(clip['movie_id'], clip['multimedia_id'].replace('.', ''))
    else:
        video_url = clip['video_url']

    return {'movie_id': clip['movie_id'], 'url': video_url, 'title': movie['title'], 'plot': f"{movie['plot'][:190]} ..."}