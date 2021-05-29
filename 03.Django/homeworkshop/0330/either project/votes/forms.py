from django import forms
from .models import Subject, Vote


class SubjectForm(forms.ModelForm):

    class Meta:
        model = Subject
        fields = '__all__'
        

class VoteForm(forms.ModelForm):
    choice = forms.ChoiceField(
        choices=[
            (1, 'BLUE'),
            (2, 'RED'),
        ],
        label='',
    )
    comment = forms.CharField(
        label='',
        widget=forms.Textarea(
            attrs={
                'rows': 2,
                'placeholder': '댓글을 작성해 주세요.',
            }
        ),
    )

    class Meta:
        model = Vote
        exclude = ('subject',)
