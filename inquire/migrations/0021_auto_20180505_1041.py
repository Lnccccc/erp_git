# Generated by Django 2.0.5 on 2018-05-05 10:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inquire', '0020_auto_20180505_1034'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='keyword',
            name='time',
        ),
        migrations.AddField(
            model_name='keyword',
            name='time2',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 5, 10, 41, 27, 322089), null=True),
        ),
    ]