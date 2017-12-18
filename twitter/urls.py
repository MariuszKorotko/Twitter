"""Twitter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.core.urlresolvers import reverse_lazy
from .views import IndexView, signup, AddMessageView, AddTweetView, \
    TweetDetailsView, UserDetailsView, UserUpdateView, UserDeleteView, \
    MessagesView
from django.contrib.auth import views as auth_views

app_name = 'twitter'

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^login/', auth_views.LoginView.as_view(
        template_name='registration/login_form.html'),
        name='login'),
    url(r'^logout/', auth_views.LogoutView.as_view(
        template_name='registration/logged_out.html'),
        name='logout'),
    url(r'^signup/$', signup, name='signup'),
    url(r'^add_tweet$', AddTweetView.as_view(), name='add_tweet'),
    url(r'^tweet_details/(?P<id>(\d)+)/$', TweetDetailsView.as_view(),
        name='tweet_details'),
    url(r'^user_details/(?P<id>(\d)+)/$', UserDetailsView.as_view(),
        name='user_details'),
    url(r'^user_update/(?P<id>(\d)+)/$', UserUpdateView.as_view(),
        name='user_update'),
    url(r'^user_delete/(?P<id>(\d)+)/$', UserDeleteView.as_view(),
        name='user_delete'),
    url(r'^password_change/$', auth_views.PasswordChangeView.as_view(
            template_name='registration/password_change_form.html',
            success_url=reverse_lazy('twitter:password_change_done')),
        name='password_change'),
    url(r'^password_change/done/$', auth_views.PasswordChangeDoneView.as_view(
            template_name='registration/password_change_done.html'),
        name='password_change_done'),
    url(r'^messages/$', MessagesView.as_view(), name='messages'),
    url(r'^add_message/(?P<id>(\d)+)/$', AddMessageView.as_view(),
        name='add_message'),
]
