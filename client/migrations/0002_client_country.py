# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-05-02 01:35
from __future__ import unicode_literals

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='country',
            field=django_countries.fields.CountryField(blank=True, max_length=2, verbose_name='Country'),
        ),
    ]
