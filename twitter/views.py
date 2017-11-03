from django.views import generic
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Tweet
from .forms import AddTweetForm


class IndexView(LoginRequiredMixin, generic.ListView):
    """Display all tweets using :view:`twitter.IndexView` create by
    :model:`auth.User` using model :model:`twitter.Tweet`.
    """
    template_name = 'twitter/index.html'

    def get_queryset(self):
        return Tweet.objects.order_by('-creation_date')[:20]


class AddTweetView(LoginRequiredMixin, View):
    """Add new tweet to datebase."""
    def get(self, request):
        form = AddTweetForm()
        context = {"form": form}
        return render(request, "twitter/add_tweet_form.html", context)

    def post(self, request):
        form = AddTweetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/twitter/')
