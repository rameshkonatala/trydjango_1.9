# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-18 06:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20170318_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='height_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='width_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, height_field=models.IntegerField(default=0), null=True, upload_to=b'', width_field=models.IntegerField(default=0)),
        ),
    ]
