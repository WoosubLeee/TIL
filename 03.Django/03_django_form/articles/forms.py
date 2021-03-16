from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class': 'title',
                'placeholder': 'Enter the title',
            }
        )
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': 'content',
                'placeholder': 'Enter the content',
            }
        )
    )

    class Meta:
        model = Article
        fields = '__all__' # ['pk', 'title', ...]  # 두 가지 방법 모두 가능
        # exclude = ('title')  특정 필드는 제외하고 싶을 때

# class ArticleForm(forms.Form):
#     REGIONS = [
#         ('sl', '서울'),
#         ('dj', '대전'),
#         ('gj', '광주'),
#         ('gm', '구미'),
#     ]
#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea)
#     region = forms.ChoiceField(choices=REGIONS, widget=forms.RadioSelect())