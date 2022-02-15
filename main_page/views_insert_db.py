from django.shortcuts import render, redirect
from user.models import UserModel
from django.contrib.auth import get_user_model  # 사용자가 데이터베이스 안에 있는 검사하는 함수
from django.contrib import auth, messages
from django.views.decorators.csrf import csrf_exempt
from .models import QuoteModel, MovieModel, RatingModel, ClipModel
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from .recommender.movie_recommender import MovieRecommender

from django.db.models import Value
from django.db.models.functions import Replace

import requests
from bs4 import BeautifulSoup
import random


def get_movie_clip_url(movie_code, multimedia_id):
    url = f"https://movie.naver.com/movie/bi/mi/mediaView.naver?code={movie_code}&mid={multimedia_id}"
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    core_url = soup.select_one('.video_ar iframe')['src']
    full_url = f"https://movie.naver.com{core_url}"
    return full_url

# Create your views here.
def main_view(request):
    if request.method == 'GET':
        movie_id  = [194204, 177366,93756,167651,85579,102875,115977,78726]
        draw_movie_id = movie_id[random.randrange(8)]
        clip = ClipModel.objects.filter(movie_id=draw_movie_id).values()[0]
        movie = MovieModel.objects.filter(movie_id=draw_movie_id).values()[0]
        print(clip)
        if clip['video_url'] == 'None':
            video_url = get_movie_clip_url(clip['movie_id'], clip['multimedia_id'].replace('.', ''))
        else:
            video_url = clip['video_url']
        print(video_url)
        return render(request, 'main_page/main_page.html', {'url': video_url, 'title': movie['title'], 'plot': f"{movie['plot'][:190]} ..."})


def testroom_view(request):
    if request.method == 'GET':
        # 명대사 db insert
        # korean_movie_qoute = pd.read_csv('login/naver_korean_movie_quote.csv', encoding='utf-8', sep=',', on_bad_lines='skip') # csv파일 불러오기
        # for i, info in enumerate(korean_movie_qoute.values):
        #     print(f'#####{info[0]} {info[1]} {i+1}')
        #     try:
        #         movie_model = MovieModel.objects.get(movie_id=f'{info[0]}')
        #         q = QuoteModel(movie_id=info[0], role=info[2], actor=info[3], quote=info[4], moviemodel=movie_model)
        #         q.save()
        #     except Exception as e:
        #         print(e)

        # 평점 db insert - 거의 2시간 걸림 헥..
        # korean_movie_ratings = pd.read_csv('login/naver_korean_movie_ratings500.csv', encoding='utf-8', sep=',', on_bad_lines='skip')
        # for i, info in enumerate(korean_movie_ratings.values):
        #     print(f'#####{info[0]} {i+1}')
        #     try:
        #         q = RatingModel(movie_id=info[0], username=info[1], rating=info[2], timestamp=info[3], comment=info[4])
        #         q.save()
        #     except Exception as e:
        #         print(e)

        # 영화 코드로 영화 명대사 로드 1
        # quotes = QuoteModel.objects.filter(movie_id='39470')
        # for quote in quotes:
        #     print(quote.quote)
        
        # 영화 코드로 영화 명대사 로드 2
        # movie = MovieModel.objects.get(movie_id='39470')
        # for quote in movie.quotemodel_set.all():
        #     print(quote.quote)
        
        # 유저 기반 협업필터링 실험실 시작
        # df_movie_info = pd.DataFrame(list(MovieModel.objects.all().values())) # 영화 정보 불러오기
        # 유저 기반 협업필터링 실험실 끝

        # 아이템기반 협업 필터링 영화 추천 목록 받아오기
        # mr = MovieRecommender()
        # movie_dict = mr.get_similar_movies_on_ibcf('161967',20)
        # print(movie_dict)

        # 잠재 요인 협업 필터링
        # movie_list = MovieRecommender().get_similar_movies_on_lfcf('161967')
        # print(movie_list)

        # 명대사 검색
        # dd = QuoteModel.objects.filter(quote__icontains='어찌내가').values()
        # input_voice = '어찌 내 가 왕이 될 상인 가'.replace(' ','')
        # dd = QuoteModel.objects.annotate(
        #     remove_blank=Replace('quote', Value(' '), Value('')),
        #     remove_period=Replace('remove_blank', Value('.'), Value('')),
        #     remove_comma=Replace('remove_period', Value(','), Value('')),
        #     remove_question=Replace('remove_comma', Value('?'), Value('')),
        #     remove_exclamation=Replace('remove_question', Value('!'), Value('')),
        #     remove_quotation=Replace('remove_exclamation', Value('\"'), Value('')),
        #     remove_apostrophe=Replace('remove_quotation', Value('\''), Value('')),
        #     remove_colon=Replace('remove_apostrophe', Value(':'), Value('')),
        #     remove_semicolon=Replace('remove_colon', Value(';'), Value('')),
        #     remove_special=Replace('remove_semicolon', Value('~'), Value('')),
        # ).filter(remove_special__icontains=input_voice)
        # for q in dd:
        #     title = MovieModel.objects.get(movie_id=q.movie_id).title
        #     print(title, q.movie_id, q.role, q.actor, q.quote)

        # 선호 영화의 장르와 같은 영화 리스트
        # movie_list = MovieRecommender().get_movies_on_same_genre('93728')
        # print(movie_list)
        # for id in movie_list:
        #     print(MovieModel.objects.filter(movie_id=id).values('movie_id', 'title', 'genre'))
        
        # 선호 영화의 감독과 같은 영화 리스트
        # movie_list = MovieRecommender().get_movies_on_same_director('93728')
        # print(movie_list)
        # for id in movie_list:
        #     print(MovieModel.objects.filter(movie_id=id).values('movie_id', 'title', 'director'))

        # 선호 영화의 배우가 출연한 영화 리스트
        # movie_dict = MovieRecommender().get_movies_on_same_actors('93728')
        # print(movie_dict)
        # for actor, movie_list in movie_dict.items():
        #     print(actor, movie_list)

        # 1월 영화 리스트 (랜덤)
        # movie_list = MovieRecommender().get_movies_on_release()
        # print(movie_list)
        # for id in movie_list:
        #     print(MovieModel.objects.filter(movie_id=id).values('movie_id', 'title', 'release'))

        # movie_list = MovieRecommender().get_movies_on_release(end_month=2, amounts=6)
        # print(movie_list)
        # for id in movie_list:
        #     print(MovieModel.objects.filter(movie_id=id).values('movie_id', 'title', 'release'))

        # 영화 클립 db insert
        # korean_movie_clip = pd.read_csv('main_page/naver_korean_movie_clip.csv', encoding='utf-8', sep=',', on_bad_lines='skip') # csv파일 불러오기
        # for i, info in enumerate(korean_movie_clip.values):
        #     print(f'#####{info[0]} {info[1]} {i+1}')
        #     try:
        #         c = ClipModel(movie_id=info[0], title=info[1], multimedia_id=info[2], video_url=info[3])
        #         c.save()
        #     except Exception as e:
        #         print(e)

        return redirect('/main')