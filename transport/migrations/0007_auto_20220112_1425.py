# Generated by Django 3.2.8 on 2022-01-12 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0006_drivers_internmechanics_mechanics'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Mechanics',
            new_name='Mechanic',
        ),
        migrations.AlterModelOptions(
            name='mechanic',
            options={'verbose_name': 'Mechanics', 'verbose_name_plural': 'Mechanics'},
        ),
    ]
