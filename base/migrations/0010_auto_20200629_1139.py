# Generated by Django 3.0.7 on 2020-06-29 11:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_auto_20200629_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='start_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 29, 11, 39, 12, 925584)),
        ),
    ]
