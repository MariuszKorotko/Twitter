from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, authenticate
from django.views import View
from django.views.generic.edit import FormView
from django.shortcuts import redirect, render
from .models import Tweet
from .forms import AddTweetForm, SignUpForm


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


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=password)
            login(request, user)
            return redirect('/twitter/')
    else:
        form = SignUpForm()
    return render(request, 'twitter/signup.html', {'form': form})


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
