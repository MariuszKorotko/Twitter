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


class AddTweetView(LoginRequiredMixin, generic.FormView):
    """Add new tweet to datebase."""
    template_name = 'twitter/add_tweet_form.html'
    form_class = AddTweetForm
    success_url = '/twitter/'

    def form_valid(self, form):
        user = self.request.user
        content = form.cleaned_data['content']
        Tweet.objects.create(content=content, user=user)
        return super(AddTweetView, self).form_valid(form)
