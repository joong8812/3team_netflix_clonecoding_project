from django.shortcuts import render
from .models import MovieModel


# Create your views here.
def recommend_movies(request):
    if request.method == 'GET':
        code = list(MovieModel.objects.filter(genre='코미디|액션').values('movie_id'))
        genre_code = []
        for i in range(12):
            genre_code.append(code[i]['movie_id'])

        print(genre_code)

        # print(list(MovieModel.objects.all().values()))
        return render(request, 'main_page.html', {'genre_code': genre_code})

