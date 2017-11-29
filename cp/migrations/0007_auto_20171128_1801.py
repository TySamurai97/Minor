# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-28 18:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cp', '0006_auto_20171124_1641'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserStats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=128)),
                ('implementation', models.IntegerField(null=True)),
                ('binarySearch', models.IntegerField(null=True)),
                ('dp', models.IntegerField(null=True)),
                ('gameTheory', models.IntegerField(null=True)),
                ('graphs', models.IntegerField(null=True)),
                ('greedy', models.IntegerField(null=True)),
                ('hashing', models.IntegerField(null=True)),
                ('math', models.IntegerField(null=True)),
                ('string', models.IntegerField(null=True)),
                ('dataStructures', models.IntegerField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='userdata',
            name='spojRating',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='userstats',
            name='userData',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cp.UserData'),
        ),
    ]