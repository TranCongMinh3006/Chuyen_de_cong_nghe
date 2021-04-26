# Generated by Django 3.1.2 on 2021-03-17 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0036_auto_20210318_0007'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='thumbnail',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='articles',
            name='time',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='articles',
            name='weight_score',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]