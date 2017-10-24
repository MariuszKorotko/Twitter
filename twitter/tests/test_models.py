from django.test import TestCase
from django.utils import timezone
from django.contrib.auth.models import User
from twitter.models import Tweet


class TweetModelTest(TestCase):
    """Testing by creating new tweet using :model:`Tweet`"""
    def create_tweet(self, content="Test Tweet!", creation_date=timezone.now(

    ), user=User()):
        user.save()
        return Tweet.objects.create(content=content,
                                    creation_date=creation_date, user=user)

    def test_tweet_creation(self):
        """Create tweet"""
        tweet = self.create_tweet()
        self.assertTrue(isinstance(tweet, Tweet))
        self.assertEqual(tweet.content, "Test Tweet!")
        self.assertEqual(tweet.creation_date, tweet.creation_date)
        self.assertEqual(tweet.user, tweet.user)
