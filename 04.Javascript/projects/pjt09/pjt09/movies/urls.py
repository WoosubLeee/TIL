from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:movie_pk>/', views.detail, name='detail'),
    path('recommended/', views.recommended, name='recommended'),
    path('recommended_temp/', views.recommended_temp, name='recommended_temp'),
    path('recommended_choice/', views.recommended_choice,
         name='recommended_choice'),
]
