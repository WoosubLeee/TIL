from django.urls import path
from . import views

app_name='community'

urlpatterns = [
    path('movies/<int:movie_pk>/', views.movie_detail),
    # 모든 영화에 대한 모든 리뷰
    path('review/', views.review_list),
    path('review/<int:review_pk>/', views.review_detail),
    path('movies/<int:movie_pk>/review/', views.review_create),
    path('movies/<int:movie_pk>/review/<int:review_pk>/', views.review_update),
    # 모든 리뷰에 대한 모든 코멘트
    path('comment/', views.comment_list),
    path('review/<int:review_pk>/comment/', views.comment_create),
    path('review/<int:review_pk>/comment/<int:comment_pk>/', views.comment_delete),
]