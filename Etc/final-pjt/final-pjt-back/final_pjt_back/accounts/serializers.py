from rest_framework import serializers
from django.contrib.auth import get_user_model


User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    email = serializers.CharField()
    class Meta:
        model = User
        fields = ('username', 'password', 'email')

class MyInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'last_login', 'email', 'date_joined')
        # fields = '__all__'
