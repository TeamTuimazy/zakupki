# Generated by Django 3.1.4 on 2020-12-18 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_customer_employee_nsifz233type_nsiikul_nsiokpo_nsippo_nsitimezone_nsitypecontact_organization_organi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='fz233type',
            field=models.ManyToManyField(null=True, to='main_app.nsiFz233type'),
        ),
    ]
