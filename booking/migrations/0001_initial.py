# Generated by Django 4.2.3 on 2023-07-23 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='BookingModel',
            fields=[
                ('booking_number', models.IntegerField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('customer_name', models.CharField(max_length=100, unique=True)),
                ('rental_datetime', models.DateTimeField()),
                ('car_mileage_request', models.DecimalField(decimal_places=2, max_digits=10)),
                ('return_datetime', models.DateTimeField()),
                ('car_mileage_return', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('rental_price', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('car_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.carcategory')),
            ],
        ),
    ]