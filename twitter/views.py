from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, authenticate
from django.core.urlresolvers import reverse_lazy
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
            'tweet_form': tweet_form,
            'tweet_list': tweet_list
        }
        return render(request, 'twitter/index.html', context)


class AddTweetView(LoginRequiredMixin, FormView):
    """Adds new tweet to db"""
    template_name = "index.html"
    form_class = AddTweetForm
    success_url = reverse_lazy('twitter:index')

    def form_valid(self, tweet_form):
        user = self.request.user
        contents = tweet_form.cleaned_data['contents']
        Tweet.objects.create(user=user,
                             contents=contents,
                             )
        return super(AddTweetView, self).form_valid(tweet_form)


class TweetDetailsView(LoginRequiredMixin, View):
    """Displays details of tweet and adds new comment to db"""
    def get(self, request, id):
        tweet = Tweet.objects.get(pk=id)
        comments_list = Comment.objects.filter(tweet_id=tweet.id,
                                               blocked=False).order_by(
                                                              '-creation_date')
        comment_form = AddCommentForm(initial={'user': request.user,
                                               'tweet': id
                                               })
        context = {
            'tweet': tweet,
            'comments_list': comments_list,
            'comment_form': comment_form
        }
        return render(request, 'twitter/tweet_details.html', context)

    def post(self, request, id):
        comment_form = AddCommentForm(request.POST)
        tweet = Tweet.objects.get(pk=id)
        if comment_form.is_valid():
            comment_form.contents = comment_form.cleaned_data['contents']
            comment_form.save()
            return redirect('/twitter/tweet_details/{}'.format(tweet.id))


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
