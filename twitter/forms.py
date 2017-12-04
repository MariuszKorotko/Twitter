from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.forms.widgets import Textarea
from twitter.models import Tweet, User


class SignUpForm(UserCreationForm):
    """Adding new user"""
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')


class AddTweetForm(ModelForm):
    """Adding new tweet."""
    class Meta:
        model = Tweet
        fields = ['content']
        widgets = {
            'content': Textarea(attrs={'cols': 60, 'rows': 3})
        }
