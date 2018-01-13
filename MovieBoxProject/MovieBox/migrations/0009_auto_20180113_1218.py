# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-13 10:18
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MovieBox', '0008_auto_20180113_1211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='votes',
            field=models.ManyToManyField(blank=True, related_name='UserMovie', to=settings.AUTH_USER_MODEL),
        ),
    ]
