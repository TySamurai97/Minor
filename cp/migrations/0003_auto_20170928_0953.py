# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-28 09:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cp', '0002_auto_20170926_1901'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='codechef',
            name='userdata',
        ),
        migrations.RemoveField(
            model_name='codeforces',
            name='userdata',
        ),
        migrations.RemoveField(
            model_name='spoj',
            name='userdata',
        ),
    ]
