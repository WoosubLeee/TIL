from os import execl
from django import forms
from .models import Reservation, Comment


class ReservationForm(forms.ModelForm):
    date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'date'
            }
    ))
    class Meta:
        model = Reservation
        fields = '__all__'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['reservation',]