from __future__ import unicode_literals
from datetime import *
from django.db import models
from django.contrib.auth.models import User


class Todo1(models.Model):
    title = models.CharField(max_length=200, null=True)
    text = models.TextField(null=True)
    create_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title


choices = [
    ('5-Star', '5-Star'),
    ('4-Star', '4-Star'),
    ('3-Star', '3-Star'),
    ('2-Star', '2-Star'),
    ('1-Star', '1-Star'),
]


class Feedback(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True)
    email = models.EmailField(max_length=50, unique=True, null=True)
    stars = models.CharField(max_length=30, choices=choices, null=True)
    message = models.TextField(null=True)

    def __str__(self):
        return self.stars


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    activation_key = models.CharField(max_length=40, blank=True)
    key_expires = models.DateTimeField()

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = u'User profiles'
