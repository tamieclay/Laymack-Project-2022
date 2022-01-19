# Generated by Django 3.2.8 on 2021-12-29 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuditReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departmentname', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('subjectofaudit', models.CharField(max_length=255)),
                ('auditdate', models.DateTimeField()),
                ('report', models.TextField()),
            ],
            options={
                'verbose_name': 'AuditReport',
                'verbose_name_plural': 'AuditReport',
            },
        ),
    ]
