# Generated by Django 3.1.4 on 2020-12-20 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0013_auto_20201219_2314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nsiokei',
            name='code',
            field=models.CharField(max_length=5, unique=True, verbose_name='Код ОКЕИ'),
        ),
        migrations.AlterField(
            model_name='nsiokeisection',
            name='code',
            field=models.CharField(max_length=5, unique=True, verbose_name='Код раздела'),
        ),
    ]
