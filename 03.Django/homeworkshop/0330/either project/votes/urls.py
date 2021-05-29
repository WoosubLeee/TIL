from django.urls import path
from . import views

app_name = 'votes'
urlpatterns = [
    path('create/', views.create, name='create'),
    path('', views.index, name='index'),
    path('<int:subject_pk>/', views.detail, name='detail'),
    path('<int:subject_pk>/vote/', views.vote, name='vote'),
    path('random/', views.random, name='random'),
]
