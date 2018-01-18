# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.conf import settings
from django.db.models.signals import post_save
from .utils import code_generator

User = settings.AUTH_USER_MODEL


class Profile(models.Model):
    user = models.OneToOneField(User)
    followers = models.ManyToManyField(User,related_name='is_following',blank=True)
    #following = models.ManyToManyField (User,related_name='is_following',blank=True)
    activated = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


def post_save_user_receiver(sender, instance, created, *args, **kwargs):
    if created:
        profile, is_created = Profile.objects.get_or_create(user=instance)

post_save.connect(post_save_user_receiver,sender=User)
