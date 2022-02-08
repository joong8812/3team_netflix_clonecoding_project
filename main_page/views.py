from django.shortcuts import render, redirect
from .models import MovieModel, ClipModel, QuoteModel
from django.views.decorators.csrf import csrf_exempt
from user.views import UserModel
from .recommender.movie_recommender import MovieRecommender
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from .stt import naverCSRRequest
from django.http import JsonResponse
import re
import json
from difflib import SequenceMatcher

import requests
from bs4 import BeautifulSoup
import random

# Create your views here.
@login_required
def recommend_movies(request):
    if request.method == 'GET':
        mr = MovieRecommender()
        user = request.user.genre_list
        a = json.loads(user)

        print(type(a))
        similar = mr.get_similar_movies_on_ibcf(a[0], 12)
        similar_recommend = MovieRecommender().get_similar_movies_on_lfcf(a[1], 12)
        similar_genre = MovieRecommender().get_movies_on_same_genre(a[0], 12)
        same_director = MovieRecommender().get_movies_on_same_director(a[1])
        on_release = MovieRecommender().get_movies_on_release(end_month=2, amounts=12)
        similar_recommend_code = []
        similar_recommend_code_2 = []
        movie_list = []
        similar_genre_code = []
        same_director_list = []
        on_release_list = []
        print(similar_genre)

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
        for f in similar_recommend_code:
            similar_recommend_dict= {}
            movie = MovieModel.objects.get(movie_id=f)
            similar_recommend_dict['movie_id'] = movie.movie_id
            similar_recommend_dict['title'] = movie.title
            similar_recommend_dict['genre'] = movie.genre
            similar_recommend_dict['maturity_rating'] = movie.maturity_rating
            similar_recommend_dict['director'] = movie.director
            similar_recommend_dict['cast'] = movie.cast
            similar_recommend_dict['plot'] = movie.plot
            similar_recommend_code_2.append(similar_recommend_dict)

        for p in same_director:
            same_director_dict= {}
            movie = MovieModel.objects.get(movie_id=p)
            same_director_dict['movie_id'] = movie.movie_id
            same_director_dict['title'] = movie.title
            same_director_dict['genre'] = movie.genre
            same_director_dict['maturity_rating'] = movie.maturity_rating
            same_director_dict['director'] = movie.director
            same_director_dict['cast'] = movie.cast
            same_director_dict['plot'] = movie.plot
            same_director_list.append(same_director_dict)

        for v in on_release:
            on_release_dict= {}
            movie = MovieModel.objects.get(movie_id=v)
            on_release_dict['movie_id'] = movie.movie_id
            on_release_dict['title'] = movie.title
            on_release_dict['genre'] = movie.genre
            on_release_dict['maturity_rating'] = movie.maturity_rating
            on_release_dict['director'] = movie.director
            on_release_dict['cast'] = movie.cast
            on_release_dict['plot'] = movie.plot
            on_release_list.append(on_release_dict)


        main_movie_clip = get_main_movie_clip()
        return render(request, 'main_page/main_page.html', {'movie_list': movie_list, 'similar_recommend_code': similar_recommend_code_2,
                                                            'similar_genre_code': similar_genre_code, 'main_movie_clip': main_movie_clip,
                                                            'same_director_list':same_director_list, 'on_release_list':on_release_list})


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

# 음성 인식
# GET
def result(request):
    if request.method == 'GET':
        receive_data = request.GET['q']
        data = json.loads("{" + receive_data + "}")
        print(data)
        return render(request, 'main_page/result.html', {'data' :data})


# POST
@csrf_exempt
def search(request):
    # # print(request.POST)
    # # data1 = request.FILES.files
    # # print(data1)
    # #
    # #
    # # # for i in data1:
    # # #     print(i)
    # #
    # # # data2 = request.get('files')
    # # # print(data2)

    if request.method == 'POST':

        data = request.body
        print('data', data)
        result = naverCSRRequest(data)
        print(result)
        search_result = search1(result['text'])
        print(search_result)

        return JsonResponse(search_result)
        #return render(request, 'sparta/result.html', context=search_result) # render 왜안되는거야ㅑㅡㅡ 빡치네 우씨



# 방법 1
def search1(receive_text):
    quote_dict = movie_id_quotes()
    result_dict = {}

    for moive_id, movie_quotes in quote_dict.items():
        for quote in movie_quotes:
            if SequenceMatcher(None, quote, receive_text).ratio() > 0.7:
                print(quote)
                print(moive_id)
                movie = MovieModel.objects.filter(movie_id=moive_id)
                print(movie.values()[0]['title'])
                result_dict[moive_id] = movie.values()[0]['title']
                break

    return result_dict


def string_filter(text):
    pass
    # filtered_string = re.sub('[-=+,#/\?:^.@*\"※~ㆍ!』'|\(\)\[\]`\'…》\"\"\'·]', '', text)
    # result_string = filtered_string.replace(' ', '')
    #
    # return result_string


def movie_id_quotes():
    quote_dict = {}
    quotes = QuoteModel.objects.all()

    tmp_list = []
    before_movie_id = 39470 # first movie id

    for q in quotes:
        if q.movie_id == str(before_movie_id):
            tmp_list.append(q.quote)
        else:
            quote_dict[before_movie_id] = tmp_list
            tmp_list = []
            tmp_list.append(q.quote)

        before_movie_id = q.movie_id

    return quote_dict

# 로그아웃
@login_required
def logout(request):
    auth.logout(request)  # 인증 되어있는 정보를 없애기
    return redirect("/")
