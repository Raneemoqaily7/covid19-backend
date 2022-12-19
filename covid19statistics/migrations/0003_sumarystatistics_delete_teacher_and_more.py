# Generated by Django 4.1.4 on 2022-12-19 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covid19statistics', '0002_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='SumaryStatistics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Country', models.CharField(max_length=30)),
                ('TotalConfirmed', models.IntegerField()),
                ('TotalDeaths', models.IntegerField()),
                ('TotalRecovered', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Teacher',
        ),
        migrations.DeleteModel(
            name='TotalStatistics',
        ),
    ]