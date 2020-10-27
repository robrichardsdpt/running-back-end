# Generated by Django 3.0 on 2020-10-27 14:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20201027_0135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='run',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='run',
            name='location',
            field=models.CharField(default='no location provided', max_length=100),
        ),
        migrations.AlterField(
            model_name='run',
            name='notes',
            field=models.CharField(default='no notes', max_length=250),
        ),
        migrations.AlterField(
            model_name='run',
            name='rpe',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='run',
            name='time',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]