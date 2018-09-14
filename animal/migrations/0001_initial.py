# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-09-14 19:53
from __future__ import unicode_literals

import animal.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fur', models.CharField(blank=True, choices=[('long', 'Long'), ('short', 'Short')], default=None, max_length=5)),
                ('animal_name', models.CharField(max_length=100)),
                ('birthdate', models.DateField(blank=True, null=True, validators=[animal.models.validate_date_birth])),
                ('sex', models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female')], max_length=6)),
                ('spay_neuter', models.CharField(blank=True, choices=[('no', 'No'), ('yes', 'Yes')], max_length=3)),
                ('spay_neuter_date', models.CharField(blank=True, max_length=100)),
                ('microchip', models.CharField(blank=True, max_length=50)),
                ('dead', models.CharField(blank=True, choices=[('no', 'No'), ('yes', 'Yes')], default='no', max_length=3)),
                ('note', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Breed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Breed',
                'verbose_name_plural': 'Breeds',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Color',
                'verbose_name_plural': 'Colors',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Specie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Specie',
                'verbose_name_plural': 'Species',
                'ordering': ('name',),
            },
        ),
        migrations.AddField(
            model_name='color',
            name='specie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animal.Specie', verbose_name='Specie'),
        ),
        migrations.AddField(
            model_name='breed',
            name='specie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animal.Specie', verbose_name='Specie'),
        ),
        migrations.AddField(
            model_name='animal',
            name='breed',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animal.Breed'),
        ),
        migrations.AddField(
            model_name='animal',
            name='color',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='animal.Color'),
        ),
        migrations.AddField(
            model_name='animal',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.Client'),
        ),
        migrations.AddField(
            model_name='animal',
            name='specie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animal.Specie'),
        ),
    ]
