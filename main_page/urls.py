from django.contrib import admin
from django.urls import path, include
from . import views



urlpatterns = [
    path('', views.recommend_movies, name='main_page'),
    path('logout/', views.logout, name='logout'),
    path('search', views.search),
    path('result/', views.result),
]
