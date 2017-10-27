from django.views import generic, View
from django.shortcuts import render
from .models import Tweet
from .forms import AddTweetForm


class IndexView(generic.ListView):
    """Display all tweets using :view:`twitter.IndexView` create by
    :model:`auth.User` using model :model:`twitter.Tweet`.
    """
    template_name = 'twitter/index.html'

    def get_queryset(self):
        return Tweet.objects.order_by('creation_date')


class AddTweetView(View):
    """Using form for new tweet"""
    def get(self, request):
        """Default date for user and creation_date"""
        form = AddTweetForm(initial={'user': request.user})
        context = {'form':form}
        return render(request, 'twitter/add_tweet_form.html', context)
