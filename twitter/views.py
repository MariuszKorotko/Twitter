from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, authenticate
from django.core.urlresolvers import reverse_lazy
from django.views import View
from django.views.generic.edit import FormView, UpdateView, DeleteView
from django.shortcuts import redirect, render
from .models import Comment, Message, Tweet, User
from .forms import AddCommentForm, AddMessageForm, AddTweetForm, SignUpForm


def signup(request):
    # Register new user to db.
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=password)
            login(request, user)
            return redirect(reverse_lazy('twitter:index'))
    else:
        form = SignUpForm()
    return render(request, 'twitter/signup.html', {'form': form})


class IndexView(LoginRequiredMixin, View):
    """Display all tweets using :view:`twitter.IndexView` create by
    :model:`auth.User` using model :model:`twitter.Tweet`.
    """
    def get(self, request):
        tweet_list = Tweet.objects.filter(blocked=False).order_by(
            '-creation_date')
        tweet_form = AddTweetForm()
        user = self.request.user
        received_messages = Message.objects.filter(receiver=user).filter(
            read_off=False).filter(blocked=False)

        context = {
            'tweet_form': tweet_form,
            'tweet_list': tweet_list,
            'received_messages': received_messages,
        }
        return render(request, 'twitter/index.html', context)


class AddTweetView(LoginRequiredMixin, FormView):
    """Add new tweet to db"""
    template_name = "twitter/index.html"
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
    """Display tweet details and adds new comment to db"""
    def get(self, request, id):
        tweet = Tweet.objects.get(pk=id)
        comments_list = Comment.objects.filter(tweet_id=tweet.id,
                                               blocked=False).order_by(
                                                              'creation_date')
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
            return redirect(reverse_lazy('twitter:tweet_details',
                                         kwargs={'id': str(tweet.id)}))


class UserDetailsView(LoginRequiredMixin, View):
    """Display user details."""
    def get(self, request, id):
        user = User.objects.get(pk=id)
        logged_user = self.request.user
        tweets = Tweet.objects.filter(user=user.id).filter(
            blocked=False).order_by('-creation_date')
        context = {
            'user': user,
            'tweet_list': tweets,
            'logged_user': logged_user,
        }
        return render(request, 'twitter/user_details.html', context)


class UserUpdateView(LoginRequiredMixin, UpdateView):
    """Display and updates account details."""
    model = User
    fields = ['email', 'first_name', 'last_name']
    template_name = "twitter/user_update_form.html"

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy('twitter:index')


class UserDeleteView(LoginRequiredMixin, DeleteView):
    """Delete user"""
    model = User
    template_name = "twitter/user_delete_confirm_form.html"
    success_url = reverse_lazy('twitter:login')

    def get_object(self, queryset=None):
        return self.request.user


class MessagesView(LoginRequiredMixin, View):
    """Display all messages sent and received."""
    def get(self, request):
        user = self.request.user
        sent_messages = Message.objects.filter(sender=user).filter(
            blocked=False)
        received_messages = Message.objects.filter(receiver=user).filter(
            blocked=False)

        context = {
            'sent_messages': sent_messages,
            'received_messages': received_messages,
        }

        return render(request, 'twitter/messages.html', context)


class AddMessageView(LoginRequiredMixin, View):
    """Add new message to db"""
    def get(self, request, id):
        sender = self.request.user
        receiver = User.objects.get(pk=id)
        message_form = AddMessageForm(initial={'sender': sender,
                                               'receiver': receiver})
        context = {
            'sender': sender,
            'receiver': receiver,
            'message_form': message_form
        }
        return render(request, 'twitter/add_message.html', context)

    def post(self, request, id):
        message_form = AddMessageForm(request.POST)
        if message_form.is_valid():
            message_form.contents = message_form.cleaned_data['contents']
            message_form.save()
            return redirect(reverse_lazy('twitter:index'))


class MessageDetailsView(LoginRequiredMixin, View):
    """Display message details and change unread message on read off message."""
    def get(self, request, id):
        message = Message.objects.get(pk=id)
        user = self.request.user

        if user == message.receiver:
            message.read_off = True
            message.save()

        context = {
            'message': message
            }
        return render(request, 'twitter/message_details.html', context)
