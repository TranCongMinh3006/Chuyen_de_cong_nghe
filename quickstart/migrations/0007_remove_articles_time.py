# Generated by Django 3.1.2 on 2021-03-11 01:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0006_auto_20210311_0810'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articles',
            name='time',
        ),
    ]
