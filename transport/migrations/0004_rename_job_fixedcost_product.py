# Generated by Django 3.2.8 on 2022-01-12 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0003_auto_20220112_1033'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fixedcost',
            old_name='job',
            new_name='product',
        ),
    ]
