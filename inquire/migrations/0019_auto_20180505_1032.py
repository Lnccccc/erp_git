# Generated by Django 2.0.5 on 2018-05-05 10:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inquire', '0018_auto_20180505_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keyword',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 5, 10, 32, 38, 862754), null=True),
        ),
    ]