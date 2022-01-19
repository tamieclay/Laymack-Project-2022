# Generated by Django 3.2.8 on 2022-01-12 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=150)),
                ('age', models.IntegerField()),
                ('job', models.CharField(max_length=150)),
                ('school', models.CharField(max_length=150)),
                ('qualifications', models.CharField(max_length=150)),
                ('workexperience', models.IntegerField()),
                ('profilepicture', models.ImageField(upload_to='')),
                ('reference', models.CharField(max_length=250)),
                ('phonenumber', models.IntegerField()),
                ('address', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name': 'Application',
                'verbose_name_plural': 'Application',
            },
        ),
        migrations.CreateModel(
            name='CurrentJobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employeename', models.CharField(max_length=150)),
                ('age', models.IntegerField()),
                ('job', models.CharField(max_length=150)),
                ('school', models.CharField(max_length=150)),
                ('qualifications', models.CharField(max_length=150)),
                ('workexperience', models.IntegerField()),
                ('profilepicture', models.ImageField(upload_to='')),
                ('reference', models.CharField(max_length=250)),
                ('phonenumber', models.IntegerField()),
                ('address', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=254)),
                ('performanceappraisal', models.CharField(max_length=150)),
                ('rating', models.DecimalField(decimal_places=2, max_digits=9)),
            ],
            options={
                'verbose_name': 'CurrentJobs',
                'verbose_name_plural': 'CurrentJobs',
            },
        ),
        migrations.CreateModel(
            name='Jobsavailable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobtype', models.CharField(max_length=200)),
                ('education', models.CharField(max_length=200)),
                ('experience', models.CharField(max_length=200)),
                ('duedate', models.DateField()),
            ],
            options={
                'verbose_name': 'Jobsavailable',
                'verbose_name_plural': 'Jobsavailable',
            },
        ),
    ]
