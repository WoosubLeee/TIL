from rest_framework import serializers
from .models import Movie, Review, Comment
from accounts.serializers import UserSerializer

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('content',)
        # fields = '__all__'
        read_only_fields = ('review',)

class CommentsSerializer(serializers.ModelSerializer):
    review_title = serializers.ReadOnlyField(source='review.title')
    review_content = serializers.ReadOnlyField(source='review.content')
    username = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Comment
        fields = ('id', 'username',
'review_title', 'review_content', 'content','created_at', 'updated_at', 'review',)



# 모든 리뷰 조회
class ReviewListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'
        # fields = ('title', 'rank',)

class ReviewsSerializer(serializers.ModelSerializer):
    movie_title = serializers.ReadOnlyField(source='movie.title')
    movie_poster_path = serializers.ReadOnlyField(source='movie.poster_path')
    movie_subtitle = serializers.ReadOnlyField(source='movie.subtitle')
    movie_userRating = serializers.ReadOnlyField(source='movie.userRating')
    username = serializers.ReadOnlyField(source='user.username')
    comment_set = CommentsSerializer(many=True, read_only=True)

    class Meta:
        model = Review
        fields = ('id', 'username', 'movie_poster_path', 'movie_subtitle', 'movie_userRating', 'comment_set',
'movie_title', 'title', 'content','created_at', 'updated_at', 'movie',)

# 상세 리뷰 조회
class ReviewSerializer(serializers.ModelSerializer):
    # 상세 리뷰에 대한 모든 코멘트
    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    user = UserSerializer(required=False)

    class Meta:
        model = Review
        fields = ('user', 'title', 'content', 'created_at', 'updated_at', 'movie', 'comment_set', 'comment_count',)
        read_only_fields = ('movie',)

# 전체 영화 목록 조회
class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'
        # fields = ('title', 'release_date',)


# 상세 영화 목록 조회
class MovieSerializer(serializers.ModelSerializer):
    # 상세 영화에 있는 모든 리뷰 조회
    review_set = ReviewSerializer(many=True, read_only=True)
    review_count = serializers.IntegerField(source='review_set.count', read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'


class MyReviewSerializer(serializers.ModelSerializer):
    movie_title = serializers.ReadOnlyField(source='movie.title')
    username = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Review
        fields = ('id', 'username', 'comment_set',
'movie_title', 'title', 'content','movie',)