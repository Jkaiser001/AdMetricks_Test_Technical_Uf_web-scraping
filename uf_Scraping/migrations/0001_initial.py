# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-29 02:03
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Money',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(max_length=10)),
                ('date', models.DateField(default=datetime.date(2017, 12, 29))),
            ],
        ),
    ]
