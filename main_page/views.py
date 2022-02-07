from django.shortcuts import render
from .models import MovieModel
from .recommender.movie_recommender import MovieRecommender

# Create your views here.
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

        return render(request, 'main_page/main_page.html', {'similar_code': similar_code, 'similar_recommend_code':similar_recommend_code,
                                                            'similar_genre_code':similar_genre_code})

