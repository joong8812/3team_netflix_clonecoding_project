from django.shortcuts import render
from .models import MovieModel
from .recommender.movie_recommender import MovieRecommender

# Create your views here.
def recommend_movies(request):
    if request.method == 'GET':
        mr = MovieRecommender()
        code = mr.get_similar_movies_on_ibcf('161967', 12)
        genre_code = []

        for i in code:
            genre_code.append(str(i))

        print(genre_code)

        return render(request, 'main_page.html', {'genre_code': genre_code})

