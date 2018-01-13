# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-13 11:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MovieBox', '0011_auto_20180113_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='description',
            field=models.TextField(default='abs', max_length=5000),
        ),
        migrations.AlterField(
            model_name='mbuserprofile',
            name='favourites',
            field=models.ManyToManyField(blank=True, related_name='Favourites', to='MovieBox.Movie'),
        ),
    ]