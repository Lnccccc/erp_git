# Generated by Django 2.0.5 on 2018-05-05 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inquire', '0007_remove_keyword_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='keyword',
            name='time',
            field=models.DateTimeField(blank=True, db_column='Time', null=True),
        ),
    ]