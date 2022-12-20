# Generated by Django 4.1.4 on 2022-12-20 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covid19statistics', '0005_alter_allrecords_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allrecords',
            name='TotalConfirmed',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='allrecords',
            name='TotalDeaths',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='allrecords',
            name='TotalRecovered',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
