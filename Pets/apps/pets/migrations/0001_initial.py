# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-29 03:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text="Your Pet's name", max_length=60)),
                ('sex', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default='male', help_text="Your Pet's sex", max_length=6)),
                ('birthday', models.DateField(help_text="Your Pet's birthday")),
                ('age', models.FloatField(help_text="Your Pet's ages")),
            ],
        ),
    ]