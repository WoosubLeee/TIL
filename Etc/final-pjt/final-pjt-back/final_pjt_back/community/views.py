from django.db import models
from django.shortcuts import render, get_list_or_404, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from movies.models import Movie, Review, Comment
from movies.serializers import MovieListSerializer, MovieSerializer, ReviewListSerializer, ReviewSerializer, CommentSerializer, ReviewsSerializer, CommentsSerializer

# Create your views here.
@api_view(['GET', 'DELETE', 'PUT'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)


@api_view(['GET'])
def review_list(request):
    reviews = get_list_or_404(Review.objects.order_by('-created_at'))
    serializers = ReviewsSerializer(reviews, many=True)
    return Response(serializers.data)


@api_view(['GET', 'DELETE', 'PUT'])
def review_detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'GET':
        serializer = ReviewsSerializer(review)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        if request.user.username == review.user.username:
            serializer = ReviewSerializer(review)
            review.delete()
            data = {
                f'{review_pk}번 게시글이 삭제되었습니다.'
            }
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        if request.user.username == review.user.username:
            serializer = ReviewsSerializer(review, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def review_create(request, movie_pk):
    if request.method == 'POST':
        movie = get_object_or_404(Movie, pk=movie_pk)
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie = movie, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    # if request.method == 'PUT':
    #     review = get_object_or_404(Review, pk=review_pk)
    #     if request.user.username == review.user.username:
    #         serializer = ReviewsSerializer(review, data=request.data)
    #         if serializer.is_valid(raise_exception=True):
    #             serializer.save()
    #             return Response(serializer.data)

@api_view(['PUT'])
def review_update(request, movie_pk, review_pk):
    if request.method == 'PUT':
        review = get_object_or_404(Review, pk=review_pk)
        if request.user.username == review.user.username:
            serializer = ReviewsSerializer(review, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)


@api_view(['GET'])
def comment_list(request):
    comments = get_list_or_404(Comment)
    serializers = CommentsSerializer(comments, many=True)
    return Response(serializers.data)


@api_view(['POST'])
def comment_create(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        user = request.user
        serializer.save(review = review, user = user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['DELETE'])
def comment_delete(request, review_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.user.username == comment.user.username:
        serializer = CommentSerializer(comment)
        comment.delete()
        data = {
            f'{comment_pk}번 게시글이 삭제되었습니다.'
        }
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
