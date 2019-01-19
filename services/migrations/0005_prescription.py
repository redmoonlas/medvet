# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-01-06 17:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0001_initial'),
        ('services', '0004_auto_20181026_2038'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=10)),
                ('value_for', models.CharField(default=1, max_length=10)),
                ('frequency', models.CharField(max_length=10)),
                ('duration', models.CharField(max_length=10)),
                ('note', models.TextField(blank=True)),
                ('consultation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.Consultation')),
                ('duration_unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prescription_duration', to='medicine.UnitOfMeasurement')),
                ('frequency_unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prescription_frequency', to='medicine.UnitOfMeasurement')),
                ('medicine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicine.Medicine')),
                ('value_for_unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prescription_value_for_unit', to='medicine.UnitOfMeasurement')),
                ('value_unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prescription_value_unit', to='medicine.UnitOfMeasurement')),
            ],
        ),
    ]
