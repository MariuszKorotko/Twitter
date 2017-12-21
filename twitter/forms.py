from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, CharField
from django.forms.widgets import HiddenInput, Textarea
from .models import Comment, Message, Tweet, User


class SignUpForm(UserCreationForm):
    """Adds new user"""
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2')


class AddTweetForm(ModelForm):
    """Adds new tweet."""
    contents = CharField(widget=Textarea(attrs={'cols': 80, 'rows': 2}),
                         label='')

    class Meta:
        model = Tweet
        fields = ['contents']


class AddCommentForm(ModelForm):
    """Adds new comment."""
    contents = CharField(widget=Textarea(attrs={'cols': 80, 'rows': 2}),
                         label='')

    class Meta:
        model = Comment
        fields = ['contents', 'tweet', 'user']
        widgets = {
            'tweet': HiddenInput(),
            'user': HiddenInput()
        }


class AddMessageForm(ModelForm):
    """Creates new message."""
    contents = CharField(widget=Textarea(attrs={'cols': 80, 'rows': 2}),
                         label='')

    class Meta:
        model = Message
        exclude = ['creation_date', 'read_off', 'blocked']
        widgets = {
            'sender': HiddenInput(),
            'receiver': HiddenInput()
        }
