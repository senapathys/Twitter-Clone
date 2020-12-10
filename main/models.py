from django.db import models
from django.contrib.auth.models import User


class Tweet(models.Model):
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    body = models.CharField(max_length=280)
    date = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='like', blank=True)

    def __str__(self):
        return self.body

    def get_likes(self):
        return self.likes.count()


class Hashtag(models.Model):
    hashtag = models.CharField(max_length=280)
    tweets = models.ManyToManyField(Tweet)

    def __str__(self):
        return self.hashtag


class Follow(models.Model):
    user = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)
    following_user = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE)
