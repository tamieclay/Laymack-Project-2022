# Generated by Django 3.2.8 on 2021-12-22 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supervisor', models.CharField(max_length=150)),
                ('job', models.TextField(max_length=350)),
                ('teamonsite', models.TextField()),
                ('materialsused', models.TextField()),
                ('site', models.ImageField(upload_to='')),
            ],
        ),
    ]
