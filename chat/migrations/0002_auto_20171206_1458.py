# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-06 14:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Likes',
            new_name='Like',
        ),
        migrations.RenameField(
            model_name='like',
            old_name='blat',
            new_name='chat',
        ),
    ]