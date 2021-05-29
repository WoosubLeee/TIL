from rest_framework_jwt.views import obtain_jwt_token
from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.signup),
    path('api-token-auth/', obtain_jwt_token),
    path('myinfo/<str:username>/', views.myinfo),
    path('myinfo/<str:username>/my-review-list', views.my_review_list),
    path('myinfo/<str:username>/my-comment-list', views.my_comment_list),
]
