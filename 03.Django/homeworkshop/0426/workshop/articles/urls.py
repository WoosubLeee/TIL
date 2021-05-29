from django.urls import path
from . import views

urlpatterns = [
    path('articles/', views.list),
    path('articles/<int:article_pk>', views.detail),
]