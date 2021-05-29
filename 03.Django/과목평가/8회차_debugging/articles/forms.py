from django import forms
from .models import Article, Comment


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('title', 'content',)


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        # 모든 필드가 아닌 content만 보여지도록 아래와 같이 바꾼다
        fields = ('content',)



