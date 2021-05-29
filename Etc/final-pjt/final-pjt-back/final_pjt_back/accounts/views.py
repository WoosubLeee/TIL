from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import User, UserSerializer, MyInfoSerializer
from rest_framework.authtoken.models import Token
from movies.models import Movie, Review, Comment
from movies.serializers import MovieListSerializer, MovieSerializer, ReviewListSerializer, ReviewSerializer, CommentSerializer, ReviewsSerializer, MyReviewSerializer

@api_view(['POST'])
def signup(request):
	#1-1. Client에서 온 데이터를 받아서
    password = request.data.get('password')
    password_confirmation = request.data.get('passwordConfirmation')
		
	#1-2. 패스워드 일치 여부 체크
    if password != password_confirmation:
        return Response({'error': '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)
		
	#2. UserSerializer를 통해 데이터 직렬화
    serializer = UserSerializer(data=request.data)
    
	#3. validation 작업 진행 -> password도 같이 직렬화 진행
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        #4. 비밀번호 해싱 후 
        user.set_password(request.data.get('password'))
        user.save()
        Token.objects.create(user=user)
        # password는 직렬화 과정에는 포함 되지만 → 표현(response)할 때는 나타나지 않는다.
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(('GET',))
def myinfo(request, username):
    person = get_object_or_404(get_user_model(), username=username)
    serializer = MyInfoSerializer(person)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(('GET',))
def my_review_list(request, username):

    person = get_object_or_404(get_user_model(), username=username)
    reviewset = person.review_set.all
    serializer = MyReviewSerializer(reviewset)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(('GET',))
def my_comment_list(request, username):

    person = get_object_or_404(get_user_model(), username=username)
    commentset = person.comment_set.all
    serializer = MyCommentSerializer(commentset)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

