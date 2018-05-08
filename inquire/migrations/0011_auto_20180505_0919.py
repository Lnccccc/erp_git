# Generated by Django 2.0.5 on 2018-05-05 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inquire', '0010_auto_20180505_0918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keyword',
            name='client',
            field=models.CharField(blank=True, db_column='Client', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='keyword',
            name='keyword',
            field=models.CharField(blank=True, db_column='Keyword', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='keyword',
            name='page',
            field=models.CharField(blank=True, db_column='Page', max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='keyword',
            name='rank',
            field=models.CharField(blank=True, db_column='Rank', max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='keyword',
            name='time',
            field=models.DateField(blank=True, db_column='Time', null=True),
        ),
        migrations.AlterField(
            model_name='keyword',
            name='urlid',
            field=models.CharField(blank=True, db_column='Urlid', max_length=20, null=True),
        ),
    ]