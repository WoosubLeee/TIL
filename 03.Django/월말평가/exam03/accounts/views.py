from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
)

# Create your views here.
def signup(request):
    # Q1-1
    # 인증된 사용자의 경우 /reservations/ 경로로 redirect된다.
    if request.user.is_authenticated:
        return redirect('reservations:index')
    # POST 방식의 요청이 들어오면
    if request.method == 'POST':
        # UserCreationForm에 데이터를 받아
        form = UserCreationForm(request.POST)
        # 데이터가 유효하다면
        if form.is_valid():
            # 저장한 후 /reservations/ 경로로 redirect하고
            form.save()
            return redirect('reservations:index')
        # 유효하지 않을 경우 아래에서 오류메시지와 함께 render를 return하게 된다.
    # GET 방식의 요청이 들어오면
    else:
        # UserCreationForm을 context에 담아 signup.html로 전달하여 render한다.
        form = UserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


def login(request):
    # Q1-2
    # 인증된 사용자의 경우 /reservations/ 경로로 redirect된다.
    if request.user.is_authenticated:
        return redirect('reservations:index')
    # POST 방식의 요청이 들어오면
    if request.method == 'POST':
        # AuthenticationForm에 데이터를 받아
        form = AuthenticationForm(request, request.POST)
        # 데이터가 유효하다면
        if form.is_valid():
            # auth_login으로 사용자를 인증하고 /reservations/ 경로로 redirect한다.
            auth_login(request, form.get_user())
            return redirect('reservations:index')
        # 유효하지 않을 경우 아래에서 오류메시지와 함께 render를 return하게 된다.
    # GET 방식의 요청이 들어오면
    else:
        # AuthenticationForm을 context에 담아 login.html로 전달하여 render한다.
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)
   

def logout(request):
    # Q1-3
    # auth_logout을 활용해 logout한 후 /accounts/login/ 경로로 redirect한다.
    auth_logout(request)
    return redirect('accounts:login')
    