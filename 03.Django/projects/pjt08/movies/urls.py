from django.urls import path
from . import views


urlpatterns = [
    path('movies/', views.movie_list),
    path('movies/<int:movie_pk>/', views.movie_detail),
    path('movies/<int:movie_pk>/reviews/', views.review_create),
    path('movies/<int:movie_pk>/reviews/<int:review_pk>/', views.review_detail),
    path('movies/<int:movie_pk>/reviews/<int:review_pk>/comments/', views.comment_create),
    path('movies/<int:movie_pk>/reviews/<int:review_pk>/comments/<int:comment_pk>', views.comment_detail),
]
