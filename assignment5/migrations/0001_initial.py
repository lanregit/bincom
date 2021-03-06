# Generated by Django 2.1 on 2020-08-15 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100, verbose_name='Full Name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('guest', models.CharField(choices=[('1 Guest', '1 Guest'), ('2 Guest', '2 Guest'), ('3 Guest', '3 Guest'), ('4 Guest', '4 Guest')], default='1 Guest', max_length=10, verbose_name='Number of guest')),
                ('message', models.TextField(verbose_name='Message')),
            ],
        ),
    ]
