# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-04 21:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_user', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('target', models.CharField(max_length=100)),
            ],
        ),
    ]
