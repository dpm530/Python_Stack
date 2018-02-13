# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-27 21:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wish_list', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlist',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='list_items', to='wish_list.User'),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='users',
            field=models.ManyToManyField(related_name='other_wish_lists', to='wish_list.User'),
        ),
    ]