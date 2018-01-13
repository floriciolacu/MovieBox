# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-13 11:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MovieBox', '0009_auto_20180113_1218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mbuser',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='mbuser', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='mbuserprofile',
            name='profile_pic',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='mbuserprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='MBUserProfile', to='MovieBox.MBUser'),
        ),
    ]