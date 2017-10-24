from django.test import TestCase
from django.utils import timezone
from django.contrib.auth.models import User
from twitter.models import Tweet


class TweetModelTest(TestCase):
    """Testing by creating new tweet using :model:`Tweet`"""
    def setUp(self):
        user = User()
        user.save()
        Tweet.objects.create(content="Test Tweet",
                             creation_date=timezone.now(), user=user)


    def test_tweet_creation(self):
        """Create and test tweet"""
        tweet = Tweet.objects.get(content="Test Tweet")
        self.assertTrue(isinstance(tweet, Tweet))
        self.assertEqual(tweet.content, "Test Tweet")
