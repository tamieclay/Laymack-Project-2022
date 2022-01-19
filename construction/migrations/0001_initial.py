# Generated by Django 3.2.8 on 2022-01-05 20:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BillOfQuantity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.CharField(max_length=100)),
                ('customer_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('billing_address', models.TextField(blank=True, null=True)),
                ('date', models.DateField()),
                ('valid_date', models.DateField(blank=True, null=True)),
                ('status', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'BillOfQuantity',
                'verbose_name_plural': 'BillOfQuantity',
            },
        ),
        migrations.CreateModel(
            name='Foundation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job', models.CharField(max_length=150)),
                ('material', models.CharField(max_length=150)),
                ('cost', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('labour', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
            ],
            options={
                'verbose_name': 'Foundation',
                'verbose_name_plural': 'Foundation',
            },
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.CharField(max_length=100)),
                ('customer_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('billing_address', models.TextField(blank=True, null=True)),
                ('date', models.DateField()),
                ('due_date', models.DateField(blank=True, null=True)),
                ('message', models.TextField(default='this is a default message.')),
                ('total_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('status', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Invoice',
                'verbose_name_plural': 'Invoice',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('address1', models.CharField(max_length=250)),
                ('address2', models.CharField(max_length=250)),
                ('city', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('postal_code', models.CharField(max_length=20)),
                ('country_code', models.CharField(blank=True, max_length=4)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('total_paid', models.DecimalField(decimal_places=2, max_digits=5)),
                ('order_key', models.CharField(max_length=200)),
                ('payment_option', models.CharField(blank=True, max_length=200)),
                ('billing_status', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Roofing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job', models.CharField(max_length=150)),
                ('material', models.CharField(max_length=150)),
                ('cost', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('labour', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
            ],
            options={
                'verbose_name': 'Roofing',
                'verbose_name_plural': 'Roofing',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preparedby', models.CharField(max_length=150)),
                ('service', models.TextField()),
                ('schedule', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Superstructure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job', models.CharField(max_length=150)),
                ('material', models.CharField(max_length=150)),
                ('cost', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('labour', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
            ],
            options={
                'verbose_name': 'Superstructure',
                'verbose_name_plural': 'Superstructure',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='construction.order')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='construction.service')),
            ],
        ),
        migrations.CreateModel(
            name='LineItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.TextField()),
                ('description', models.TextField()),
                ('quantity', models.IntegerField()),
                ('rate', models.DecimalField(decimal_places=2, max_digits=9)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=9)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='construction.invoice')),
            ],
            options={
                'verbose_name': 'LineItem',
                'verbose_name_plural': 'LineItem',
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.TextField()),
                ('description', models.TextField()),
                ('quantity', models.CharField(max_length=150)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=9)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='construction.billofquantity')),
            ],
            options={
                'verbose_name': 'Job',
                'verbose_name_plural': 'Job',
            },
        ),
        migrations.AddField(
            model_name='billofquantity',
            name='foundation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='construction.foundation'),
        ),
        migrations.AddField(
            model_name='billofquantity',
            name='roofing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='construction.roofing'),
        ),
        migrations.AddField(
            model_name='billofquantity',
            name='superstructure',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='construction.superstructure'),
        ),
    ]
