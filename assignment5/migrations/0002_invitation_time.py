# Generated by Django 2.1 on 2020-08-15 16:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('assignment5', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='invitation',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]