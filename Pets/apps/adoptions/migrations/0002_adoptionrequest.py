# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-08 00:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adoptions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdoptionRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pets_number', models.IntegerField()),
                ('reason', models.TextField()),
                ('adopter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='adoptions.AdoptionPersonInfo')),
            ],
        ),
    ]
