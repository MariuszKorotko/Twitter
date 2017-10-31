from django.forms import ModelForm
from django.forms.widgets import Textarea
from twitter.models import Tweet


class AddTweetForm(ModelForm):
    """Adding new tweet using Model Form."""
    class Meta:
        model = Tweet
        fields = ['content']
        widgets = {
            'content': Textarea(attrs={'cols': 80, 'rows': 5}),
        }
