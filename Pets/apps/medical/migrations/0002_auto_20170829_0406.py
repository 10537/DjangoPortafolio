# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-29 04:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medical', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicalinfo',
            name='vaccines',
            field=models.ManyToManyField(to='medical.Vaccines'),
        ),
    ]