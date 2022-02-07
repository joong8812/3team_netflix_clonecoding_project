from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


# Create your models here.
class UserModel(AbstractUser):
    class Meta:
        db_table = "my_user"

    username = models.CharField(
        max_length=150,
        blank=True,
        null=True,
    )
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    genre_list = models.CharField(max_length=256, default='')

    bio = models.CharField(max_length=256, default='')
    follow = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followee')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
