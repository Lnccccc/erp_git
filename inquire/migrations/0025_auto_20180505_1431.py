# Generated by Django 2.0.5 on 2018-05-05 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inquire', '0024_auto_20180505_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keyword',
            name='time2',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
