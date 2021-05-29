from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth import get_user_model
from django.views.decorators.http import require_POST
from .forms import CustomUserCreationForm, CustomProfileForm

User = get_user_model()
# Create your views here.
def signup(request):
    if request.user.is_authenticated:
        return redirect('community:index')
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('community:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'community:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)

@require_POST
def logout(request):
    auth_logout(request)
    return redirect('community:index')


def profile(request, user_id):
    person = get_object_or_404(get_user_model(), id=user_id)
    reviews = person.review_set.all()
    comments = person.comment_set.all()
    if request.method == 'POST':
        form = CustomProfileForm(request.POST,request.FILES, instance=person)
        if form.is_valid():
            form.save()
            return redirect('accounts:profile', user_id)
    else: 
        form = CustomProfileForm(instance=person)
    context = {
        'person': person,
        'form' : form,
        'reviews' : reviews,
        'comments' : comments,
        }
    return render(request, 'accounts/profile.html', context)


def follow(request, user_id):
    if request.user.is_authenticated:
        person = get_object_or_404(get_user_model(), id=user_id)
        if person.followers.filter(id=request.user.id).exists():
            person.followers.remove(request.user)
        else:
            person.followers.add(request.user)
        return redirect('accounts:profile', user_id)
    return redirect('accounts:login')
