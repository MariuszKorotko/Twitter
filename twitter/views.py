from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, authenticate
from django.views import View
from django.views.generic.edit import FormView
from django.shortcuts import redirect, render
from .models import Comment, Tweet, User
from .forms import AddCommentForm, AddTweetForm, SignUpForm


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


class IndexView(LoginRequiredMixin, View):
    """Displays all tweets using :view:`twitter.IndexView` create by
    :model:`auth.User` using model :model:`twitter.Tweet`.
    """
    def get(self, request):
        tweet_list = Tweet.objects.order_by('-creation_date')
        tweet_form = AddTweetForm()
        context = {
            'form': tweet_form,
            'tweet_list': tweet_list
        }
        return render(request, 'twitter/index.html', context)


class AddTweetView(LoginRequiredMixin, FormView):
    """Adds new tweet to db"""
    template_name = "index.html"
    form_class = AddTweetForm
    success_url = '/twitter/'

    def form_valid(self, form):
        user = self.request.user
        contents = form.cleaned_data['contents']
        Tweet.objects.create(user=user,
                             contents=contents,
                             )
        return super(AddTweetView, self).form_valid(form)


class TweetDetailsView(LoginRequiredMixin, View):
    """Displays details of tweet."""
    def get(self, request, id):
        tweet = Tweet.objects.get(pk=id)
        comments_list = Comment.objects.filter(tweet_id=tweet.id).order_by(
            '-creation_date')
        comment_form = AddCommentForm()
        context = {
            'tweet': tweet,
            'comments': comments_list,
            'comment_form': comment_form
        }
        return render(request, 'twitter/tweet_details.html', context)


class UserDetailsView(LoginRequiredMixin, View):
    """Displays details of user"""
    def get(self, request, id):
        user = User.objects.get(pk=id)
        tweets = Tweet.objects.filter(user_id=user.id).order_by(
            '-creation_date')
        context = {
            'user': user,
            'tweet_list': tweets
        }
        return render(request, 'twitter/user_details.html', context)
