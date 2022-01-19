# Generated by Django 3.2.8 on 2022-01-04 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Labour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.CharField(max_length=255)),
                ('labourhours', models.DecimalField(decimal_places=2, max_digits=9)),
                ('rate', models.DecimalField(decimal_places=2, max_digits=9)),
                ('labour', models.DecimalField(decimal_places=2, max_digits=9)),
            ],
        ),
    ]
