from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.forms.widgets import Textarea
from twitter.models import Comment, Tweet, User


class SignUpForm(UserCreationForm):
    """Adds new user"""
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')


class AddTweetForm(ModelForm):
    """Adds new tweet."""
    class Meta:
        model = Tweet
        fields = ['contents']
        widgets = {
            'contents': Textarea(attrs={'cols': 40, 'rows': 4})
        }


class AddCommentForm(ModelForm):
    """Adds new comment"""
    class Meta:
        model = Comment
        fields = ['contents']
        widgets = {
            'contents': Textarea(attrs={'cols': 40, 'rows': 2})
        }