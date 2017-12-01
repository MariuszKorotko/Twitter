from django.forms import ModelForm
from django.forms.widgets import Textarea
from twitter.models import Tweet, User


class AddTweetForm(ModelForm):
    """Adding new tweet."""
    class Meta:
        model = Tweet
        fields = ['content']
        widgets = {
            'content': Textarea(attrs={'cols': 60, 'rows': 3})
        }
