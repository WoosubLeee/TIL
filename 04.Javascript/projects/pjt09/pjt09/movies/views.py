from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator
from django.core import serializers
from .models import Movie, Genre
from random import sample


# Create your views here.
@require_GET
def index(request):
    movies = Movie.objects.all()
    paginator = Paginator(movies, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'movies': movies,
        'page_obj': page_obj,
    }
    return render(request, 'movies/index.html', context)


@require_GET
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    context = {
        'movie': movie,
    }
    return render(request, 'movies/detail.html', context)


@require_GET
def recommended(request):
    movies = Movie.objects.all()
    movies = sample(list(movies), 10)
    context = {
        'movies': movies,
    }
    return render(request, 'movies/recommended.html', context)


@require_GET
def recommended_temp(request):
    genres = Genre.objects.all()
    movies = Movie.objects.all()
    context = {
        'genres': genres,
        'movies': movies,
    }
    return render(request, 'movies/recommended_temp.html', context)


def recommended_choice(request):
    movies = Movie.objects.all()
    movie_list = {
        'movies': movies,
    }
    data = serializers.serialize('json', movies)
    return HttpResponse(data, content_type='application/json')
