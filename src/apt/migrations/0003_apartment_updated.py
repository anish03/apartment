# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-01-16 08:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apt', '0002_apartment_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartment',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]