from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from rest_framework.serializers import Serializer
from .models import Movie, Review, Comment
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import MovieListSerializer, MovieSerializer
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_GET, require_POST, require_http_methods

# Create your views here.

@api_view(['GET', 'POST'])
def index(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = MovieListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


@api_view(['GET'])
# @authentication_classes([JSONWebTokenAuthentication])
# @permission_classes([IsAuthenticated])
def recommended_latest(request):

    recent_movies = Movie.objects.order_by('-release_date')[:30]
    recent_serializer = MovieListSerializer(recent_movies, many=True)
    return Response(recent_serializer.data)




@api_view(['GET'])
# @authentication_classes([JSONWebTokenAuthentication])
# @permission_classes([IsAuthenticated])
def recommended_rated(request):

    rated_movies = Movie.objects.order_by('-userRating')[:30]
    rated_serializer = MovieListSerializer(rated_movies, many=True)
    return Response(rated_serializer.data)



def my_like(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    user = request.user
    if user.like_movies.filter(pk=movie.pk).exists():
        user.like_movies.remove(movie)
        liked = False
    else:
        user.like_movies.add(movie)
        liked = True

    like_serializer = MovieListSerializer(user.like_movies, many=True)
    return Response(like_serializer.data)


@require_POST
def like(request, movie_pk):
    # if request.user.is_authenticated:
    movie = get_object_or_404(Movie, pk=movie_pk)
    user = request.user

    if movie.like_users.filter(pk=user.pk).exists():
        movie.like_users.remove(user)
        liked = False
    else:
        movie.like_users.add(user)
        liked = True
    serializer = MovieSerializer(movie)
    return Response(serializer.data)
