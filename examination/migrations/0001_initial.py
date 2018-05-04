# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-05-04 00:01
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('animal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anatomopathology',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Anatomopathology',
            },
        ),
        migrations.CreateModel(
            name='Electrolytes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Electrolytes',
                'verbose_name_plural': 'Electrolytes',
            },
        ),
        migrations.CreateModel(
            name='Endocrinology',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Endocrinology',
            },
        ),
        migrations.CreateModel(
            name='Hematology',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Hematology',
            },
        ),
        migrations.CreateModel(
            name='HepaticProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Hepatic profile',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Image',
            },
        ),
        migrations.CreateModel(
            name='Microbiology',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Microbiology',
            },
        ),
        migrations.CreateModel(
            name='Other',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Other',
            },
        ),
        migrations.CreateModel(
            name='Parasitological',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Parasitological',
            },
        ),
        migrations.CreateModel(
            name='Proteins',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Proteins',
                'verbose_name_plural': 'Proteins',
            },
        ),
        migrations.CreateModel(
            name='RenalProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Renal profile',
            },
        ),
        migrations.CreateModel(
            name='RequestForExamination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('anatomopathology_exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='examination.Anatomopathology')),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animal.Animal', verbose_name="Animal's Name")),
                ('electrolytes_exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='examination.Electrolytes')),
                ('endocrinology_exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='examination.Endocrinology')),
                ('hematology_exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='examination.Hematology')),
                ('hepatic_profile_exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='examination.HepaticProfile')),
                ('image_exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='examination.Image')),
                ('microbiology_exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='examination.Microbiology')),
                ('other_exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='examination.Other')),
                ('parasitological_exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='examination.Parasitological')),
                ('proteins_exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='examination.Proteins')),
                ('renal_profile_exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='examination.RenalProfile')),
            ],
            options={
                'ordering': ('date',),
                'verbose_name': 'Request for examination',
                'verbose_name_plural': 'Requests for examination',
            },
        ),
    ]
