# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-24 20:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_secrets', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='test',
        ),
    ]