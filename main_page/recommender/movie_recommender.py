import pandas as pd
from main_page.models import MovieModel, RatingModel
# from surprise import dump
from django.db.models import Q
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