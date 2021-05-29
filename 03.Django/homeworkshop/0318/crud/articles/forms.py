from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter the Title',
                'maxlength': 10,
            }
        )
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Enter the Content',
                'rows': 5,
                'cols': 30,
            }
        )
    )

    class Meta:
        model = Article
        fields = '__all__'