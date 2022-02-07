from django.shortcuts import render
from .models import MovieModel
from .recommender.movie_recommender import MovieRecommender

# Create your views here.
def recommend_movies(request):
    if request.method == 'GET':
        mr = MovieRecommender()
        code = mr.get_similar_movies_on_ibcf('161967', 12)
        genre_code = []
        movie_list = MovieRecommender().get_similar_movies_on_lfcf('161967')

        for i in code:
            genre_code.append(str(i))

        print(movie_list)

        return render(request, 'main_page.html', {'genre_code': genre_code, 'movie_list':movie_list})

