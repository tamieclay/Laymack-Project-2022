# Generated by Django 3.2.8 on 2022-01-12 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0004_rename_job_fixedcost_product'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='trip',
            options={'verbose_name': 'Trip', 'verbose_name_plural': 'Trip'},
        ),
    ]
