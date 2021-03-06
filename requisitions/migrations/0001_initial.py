# Generated by Django 3.2.8 on 2022-01-12 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Requisition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(max_length=150)),
                ('date', models.DateField()),
                ('purpose', models.CharField(max_length=300)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('preparedby', models.CharField(max_length=100)),
                ('quotation1', models.ImageField(upload_to='')),
                ('quotation2', models.ImageField(upload_to='')),
                ('quotation3', models.ImageField(upload_to='')),
            ],
            options={
                'verbose_name': 'Requisition',
                'verbose_name_plural': 'Requisition',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('approved', 'APPROVED'), ('pending', 'PENDING'), ('rejected', 'REJECTED')], default='pending', max_length=10)),
                ('comment', models.CharField(max_length=150)),
                ('budget', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='requisitions.requisition')),
            ],
            options={
                'verbose_name': 'Review',
                'verbose_name_plural': 'Review',
            },
        ),
    ]
