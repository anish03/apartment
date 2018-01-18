# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-01-17 22:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20180117_2234'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='following',
        ),
        migrations.AlterField(
            model_name='profile',
            name='followers',
            field=models.ManyToManyField(blank=True, related_name='is_following', to=settings.AUTH_USER_MODEL),
        ),
    ]
