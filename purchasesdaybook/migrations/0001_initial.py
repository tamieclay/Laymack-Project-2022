# Generated by Django 3.2.8 on 2021-12-29 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Purchasesdaybook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('details', models.TextField()),
                ('invoicenumber', models.IntegerField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=9)),
            ],
            options={
                'verbose_name': 'Purchasesdaybook',
                'verbose_name_plural': 'Purchasesdaybook',
            },
        ),
    ]
