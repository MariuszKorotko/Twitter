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
from django.conf.urls import url, include
from .views import IndexView, signup, AddTweetView, TweetDetailsView, \
    UserDetailsView, UserUpdateView, UserDeleteView

app_name = 'twitter'

urlpatterns = [
    url('^', include('django.contrib.auth.urls')),
    url(r'^$', IndexView.as_view(), name='index'),
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
]
