from django.db import models

# Create your models here.
class MovieModel(models.Model):
    class Meta:
        db_table = 'movie'

    # code,title,genre,duration,release,maturity_rating,director,cast,plot
    movie_id = models.CharField(max_length=6, unique=True)
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100, null=True)
    duration = models.CharField(max_length=3, null=True)
    release = models.CharField(max_length=8, null=True)
    maturity_rating = models.CharField(max_length=8, null=True)
    director = models.CharField(max_length=20)
    cast = models.CharField(max_length=100)
    plot = models.CharField(max_length=65535, null=True)
    like_movie_id = models.CharField(max_length=65535, null=True)
    dislike_movie_id = models.CharField(max_length=65535, null=True)


class QuoteModel(models.Model):
    class Meta:
        db_table = 'quote'

    # code,title,role,actor,quote
    movie_id = models.CharField(max_length=6)
    role = models.CharField(max_length=20, null=True)
    actor = models.CharField(max_length=10, null=True)
    quote = models.CharField(max_length=500, null=True)
    moviemodel = models.ForeignKey(MovieModel, on_delete=models.CASCADE)


class RatingModel(models.Model):
    class Meta:
        db_table = 'rating'

    # code, userid, rating, timestamp, comment
    movie_id = models.CharField(max_length=6)
    username = models.CharField(max_length=150, null=True, blank=True)
    rating = models.CharField(max_length=2)
    timestamp = models.CharField(max_length=12)
    comment = models.CharField(max_length=65535, null=True)