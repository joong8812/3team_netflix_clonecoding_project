from django.shortcuts import render, redirect
from .models import MovieModel, ClipModel

from .recommender.movie_recommender import MovieRecommender
from django.contrib.auth.decorators import login_required
from django.contrib import auth

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
        similar_genre = MovieRecommender().get_movies_on_same_genre('93728', 12)
        similar_recommend_code = []
        movie_list = []
        similar_genre_code = []
        for i in similar:
            movie_info = {}
            movie = MovieModel.objects.get(movie_id=i)
            movie_info['movie_id'] = movie.movie_id
            movie_info['title'] = movie.title
            movie_info['genre'] = movie.genre
            movie_info['maturity_rating'] = movie.maturity_rating
            movie_info['director'] = movie.director
            movie_info['cast'] = movie.cast
            movie_info['plot'] = movie.plot
            movie_list.append(movie_info)

        for g in similar_genre:
            movie_ginfo = {}
            movie = MovieModel.objects.get(movie_id=g)
            movie_ginfo['movie_id'] = movie.movie_id
            movie_ginfo['title'] = movie.title
            movie_ginfo['genre'] = movie.genre
            movie_ginfo['maturity_rating'] = movie.maturity_rating
            movie_ginfo['director'] = movie.director
            movie_ginfo['cast'] = movie.cast
            movie_ginfo['plot'] = movie.plot
            similar_genre_code.append(movie_ginfo)
        for i in range(12):
            similar_recommend_code.append(str(similar_recommend[i][1]))

        main_movie_clip = get_main_movie_clip()
        return render(request, 'main_page/main_page.html', {'movie_list': movie_list, 'similar_recommend_code': similar_recommend_code,
                                                            'similar_genre_code': similar_genre_code, 'main_movie_clip': main_movie_clip})


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

# 로그아웃
@login_required
def logout(request):
    auth.logout(request)  # 인증 되어있는 정보를 없애기
    return redirect("/")
