from django import forms
from .models import Movie


class MovieForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class': 'title form-control',
                'placeholder': '제목을 입력해주세요.',
                'max_length': 100,
            }
        ),
        error_messages={
            'required': '제목은 필수 사항입니다.',
        }
    )
    overview = forms.CharField(
        label='줄거리',
        widget=forms.Textarea(
            attrs={
                'class': 'overview form-control',
                'placeholder': '줄거리를 입력하세요.',
                'rows': 5,
                'cols': 30,
            }
        ),
        error_messages={
            'required': '줄거리는 필수 사항입니다.',
        }
    )
    poster_path = forms.CharField(
        label='포스터 경로',
        widget=forms.TextInput(
            attrs={
                'class': 'poster_path form-control',
                'placeholder': '포스터 경로를 입력하세요.',
            }
        ),
        error_messages={
            'required': '포스터 경로는 필수 사항입니다.',
        }
    )

    class Meta:
        model = Movie
        fields = '__all__'
