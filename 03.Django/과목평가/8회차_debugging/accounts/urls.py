from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('delete/', views.delete, name='delete'),
    path('update/', views.update, name='update'),
    path('password/', views.change_password, name='change_password'),
    # variable routing을 사용하는 '<username>/' 경로 떄문에 setting이 이름으로 인식되어 오류가 발생한다
    # 이에 순서를 바꾸어주면 된다
    path('setting/', views.setting, name='setting'),
    path('<username>/', views.profile, name='profile'),
    path('<int:user_pk>/follow/', views.follow, name='follow'),
]
