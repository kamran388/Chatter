# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models


class Chat(models.Model):
    text = models.TextField()
    created_on = models.DateTimeField(auto_now_add = True)
    via = models.URLField(blank = True)
    created_by = models.ForeignKey(User)

    def total_likes(self):
        return self.like_set.count()

    def __str__(self):
        return self.text[:20]


class Like(models.Model):
    chat = models.ForeignKey(Chat)

class Profile(models.Model):
    user = models.OneToOneField(User)
    bio = models.TextField(blank=True)
    blog = models.URLField(blank=True)
