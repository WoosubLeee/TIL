from django.urls import path
from . import views  # 명시적 상대경로 표현

urlpatterns = [
    path('index/', views.index, name='index'),
    path('greeting/', views.greeting, name='greeting'),
    path('dinner/', views.dinner, name='dinner'),
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),
    path('hello/<str:name>/', views.hello, name='hello'),
    path('introduce/<str:name>/<int:age>/', views.introduce, name='introduce'),
    path('image/', views.image, name='image'),
    path('fake_google/', views.fake_google, name='fake_google'),
    path('multiply/<int:num1>/<int:num2>/', views.multiply, name='multiply'),
]