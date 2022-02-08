from django.urls import path
from . import views



urlpatterns = [
    path('', views.recommend_movies, name='main_page'),

]
