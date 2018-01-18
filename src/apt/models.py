# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db.models.signals import pre_save
from .utils import unique_slug_generator
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.urlresolvers import reverse

User = settings.AUTH_USER_MODEL

class apartment(models.Model):

    owner = models.ForeignKey(User)
    apt_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=30)
    address = models.CharField(max_length=120)
    rating = models.IntegerField(validators=[MinValueValidator(0),
                                       MaxValueValidator(5)])
    capacity = models.IntegerField(validators=[MinValueValidator(2),
                                              MaxValueValidator(7)])
    amenities = models.CharField(max_length=500)
    lat = models.FloatField(default=0)
    long = models.FloatField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(null=True,blank=True)


    def get_absolute_url(self):
        return reverse('apartment-detail',kwargs={'slug':self.slug})

    @property
    def title(self):
        return self.name

def rl_pre_save(sender,instance,*args,**kwargs):

    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(rl_pre_save,sender=apartment)
