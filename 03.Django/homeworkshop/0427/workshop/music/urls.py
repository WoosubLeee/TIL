from django.urls import path
from . import views

urlpatterns = [
    path('artists/', views.artists_list),
    path('artists/<int:artist_pk>/', views.artist_detail),
    path('artists/<int:artist_pk>/music/', views.save_music),
    path('music/', views.music_list),
    path('music/<int:music_pk>/', views.music_detail),
]