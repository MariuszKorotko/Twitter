from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic.edit import FormView
from django.shortcuts import render
from .models import Tweet
from .forms import AddTweetForm


class IndexView(LoginRequiredMixin, View):
    """Display all tweets using :view:`twitter.IndexView` create by
    :model:`auth.User` using model :model:`twitter.Tweet`.
    """
    def get(self, request):
        tweet_list = Tweet.objects.order_by('-creation_date')
        form = AddTweetForm()
        context = {
            'form': form,
            'tweet_list': tweet_list
        }
        return render(request, 'twitter/index.html', context)


class AddUserView(FormView):
    """Display form to create new user."""
    def get(self, request):
        return render(request, 'twitter/new_user.html', context=None)


class AddTweetView(LoginRequiredMixin, FormView):
    """Adds new tweet to db"""
    template_name = "index.html"
    form_class = AddTweetForm
    success_url = '/twitter/'

    def form_valid(self, form):
        user = self.request.user
        content = form.cleaned_data['content']
        Tweet.objects.create(user=user,
                             content=content,
                             )
        return super(AddTweetView, self).form_valid(form)
