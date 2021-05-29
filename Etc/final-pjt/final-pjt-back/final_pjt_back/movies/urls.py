from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:movie_pk>/', views.detail, name='detail'),
    path('<int:movie_pk>/like/', views.like, name='like'),
    path('recommended/rated', views.recommended_rated, name='recommended_rated'),
    path('recommended/latest', views.recommended_latest, name='recommended_latest'),
    path('my_like/', views.my_like, name='my_like')
]
