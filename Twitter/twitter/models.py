from django.db import models
from django.contrib.auth.models import User


class Tweet(models.Model):
    """Stores a single tweet, related to :model:`auth.User`."""
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)