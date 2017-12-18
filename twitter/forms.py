from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.forms.widgets import HiddenInput, Textarea
from twitter.models import Comment, Message, Tweet, User


class SignUpForm(UserCreationForm):
    """Adds new user"""
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2')


class AddTweetForm(ModelForm):
    """Adds new tweet."""
    class Meta:
        model = Tweet
        fields = ['contents']
        widgets = {
            'contents': Textarea(attrs={'cols': 40, 'rows': 4})
        }


class AddCommentForm(ModelForm):
    """Adds new comment."""
    class Meta:
        model = Comment
        fields = ['contents', 'tweet', 'user']
        widgets = {
            'contents': Textarea(attrs={'cols': 40, 'rows': 2}),
            'tweet': HiddenInput(),
            'user': HiddenInput()
        }


class AddMessageForm(ModelForm):
    """Creates new message."""
    class Meta:
        model = Message
        exclude = ['creation_date', 'read_off']
        widgets = {
            'contents': Textarea(attrs={'cols': 40, 'rows': 2}),
            'sender': HiddenInput(),
            'receiver': HiddenInput()
        }
