# Generated by Django 2.0.5 on 2018-05-06 08:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inquire', '0039_auto_20180506_0800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keyword',
            name='time2',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 5, 6, 8, 3, 21, 17255), null=True),
        ),
    ]