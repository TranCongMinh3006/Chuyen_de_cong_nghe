# Generated by Django 3.1.7 on 2021-03-23 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0038_auto_20210318_0052'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Category',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('userID', models.IntegerField()),
                ('categoryID', models.IntegerField()),
                ('countj', models.IntegerField()),
            ],
            options={
                'db_table': 'user_category',
            },
        ),
    ]