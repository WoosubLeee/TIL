from django.db import models
from django.conf import settings
from django.db.models.fields import related

class Movie(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    pubDate = models.CharField(max_length=100)
    image = models.CharField(max_length=200)
    userRating = models.CharField(max_length=100)
    actor = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    poster_path = models.CharField(max_length=200)
    release_date = models.CharField(max_length=200)
    genre_ids = models.CharField(max_length=200)
    movie_id = models.IntegerField()
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')


    def __str__(self):
        return self.title

class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user")
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)