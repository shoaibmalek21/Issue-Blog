# Generated by Django 3.0.7 on 2020-06-22 15:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_auto_20200622_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='date_commit',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 22, 15, 39, 36, 593321)),
        ),
        migrations.AlterField(
            model_name='agent',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 22, 15, 39, 36, 593265)),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 22, 15, 39, 36, 591922)),
        ),
    ]