import pandas as pd
from main_page.models import MovieModel, RatingModel
from surprise import dump
from django.db.models import Q, DateField
from django.db.models.functions import Cast
import random

class MovieRecommender:
    def __init__(self):
        print('MovieRecommender Hi')

    # 아이템 기반 협업 필터링 (ibcf: Item Based Collaborative Filtering)
    def get_similar_movies_on_ibcf(self, movie_id, amounts=10):
        item_based_collab = pd.read_csv('main_page/recommender/ibcf_cosine_similarity.csv')
        item_based_collab = item_based_collab.set_index('code')
        recommend_movie_dict = dict(item_based_collab[movie_id].sort_values(ascending=False)[:amounts])
        return recommend_movie_dict


    # 잠재요인 협업 필터링 (lfcf: Latent Factor Collaborative Filtering)
    def get_similar_movies_on_lfcf(self, movie_id, amounts=10):
        # 1. 선호하는 영화를 평점 10점 준 유저 찾기
        good_user_list = []
        for rate in range(11, 0, -1):
            good_user_list = RatingModel.objects.filter(Q(movie_id=movie_id) & Q(rating=str(rate)))
            if len(good_user_list) > 0:
                break
        username = good_user_list[random.randrange(0, len(good_user_list))].username

        # 2. 잠재 요인 협업 필터링 모델 로드
        pred, algo = dump.load('main_page/recommender/lfcf_recommender')
        
        # 3. 전체 영화 정보 DB에서 가져오기
        movie_info = MovieModel.objects.all()
        preds = []
        for info in movie_info:
            pred = algo.predict(username, int(info.movie_id))
            preds.append((pred.est, pred.iid)) # 각 영화 평점 예측, 영화아이디 리스트에 넣기
        preds.sort(reverse=True) # 평점 내림차순으로 정렬
        return preds[:amounts]


    # 선호하는 영화 장르와 같은 영화 리스트(random)
    def get_movies_on_same_genre(self, movie_id, amounts=10):
        movie_list = []
        genres = MovieModel.objects.get(movie_id=movie_id).genre.split('|') # 영화 장르 찾기
        for genre in genres:
            movie_list.append(MovieModel.objects.filter(genre=genre).values())
        random_list = []
        for _ in range(amounts):
            genre_count = len(movie_list)
            random_index = random.randrange(genre_count)
            random_list.append(movie_list[random_index][random.randrange(0, len(movie_list[random_index]))]['movie_id'])
        return random_list


    # 선호하는 영화의 감독이 만든 영화 리스트
    def get_movies_on_same_director(self, movie_id):
        director = MovieModel.objects.get(movie_id=movie_id).director # 영화 감독 찾기
        movie_list = list(MovieModel.objects.filter(director=director).values_list('movie_id', flat=True))
        return movie_list


    # 선호하는 영화의 출연한 배우가 출연한 다른 작품 리스트
    def get_movies_on_same_actors(self, movie_id):
        actors = MovieModel.objects.get(movie_id=movie_id).cast.split('|') # 영화 배우 찾기
        movie_dict = {}
        for actor in actors:
            movie_list = list(MovieModel.objects.filter(cast__contains=actor).values_list('movie_id', flat=True))
            movie_dict[actor] = movie_list
        return movie_dict


    # 조건에 따른 월 기간별 개봉 영화 리스트(random)
    def get_movies_on_release(self, start_month=1, end_month=1, amounts=10):
        random_list = []
        movie_list = MovieModel.objects.all().annotate(
            release_date=Cast('release', output_field=DateField()),
        ).filter(
            release_date__month__gte=start_month,
            release_date__month__lte=end_month
        )
        for _ in range(amounts):
            random_list.append(movie_list[random.randrange(0, len(movie_list))].movie_id)
        return random_list