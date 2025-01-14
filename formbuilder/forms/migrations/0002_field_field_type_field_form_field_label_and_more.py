# Generated by Django 5.1.4 on 2025-01-03 17:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='field',
            name='field_type',
            field=models.CharField(choices=[('text', 'Text'), ('number', 'Number'), ('date', 'Date')], default='text', max_length=20),
        ),
        migrations.AddField(
            model_name='field',
            name='form',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fields', to='forms.form'),
        ),
        migrations.AddField(
            model_name='field',
            name='label',
            field=models.CharField(default='Default Label', max_length=100),
        ),
        migrations.AddField(
            model_name='field',
            name='required',
            field=models.BooleanField(default=True),
        ),
    ]
