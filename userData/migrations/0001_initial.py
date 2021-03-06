# Generated by Django 2.2.1 on 2019-05-10 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderID', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=30)),
                ('address1', models.CharField(max_length=100)),
                ('address2', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('zipcode', models.CharField(max_length=30)),
                ('thread1', models.CharField(max_length=60)),
                ('denim1', models.CharField(max_length=60)),
                ('cut1', models.CharField(max_length=30)),
                ('denim2', models.CharField(max_length=60)),
                ('thread2', models.CharField(max_length=60)),
                ('cut2', models.CharField(max_length=30)),
                ('prevMeasurement', models.CharField(max_length=30)),
                ('tailorId', models.CharField(max_length=30)),
                ('dateOfMeasurement', models.CharField(max_length=30)),
                ('timeOfMeasurement', models.CharField(max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('paymentType', models.CharField(max_length=30)),
                ('paymentId', models.CharField(max_length=30)),
                ('status', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='tempOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderID', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=30)),
                ('address1', models.CharField(max_length=100)),
                ('address2', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('zipcode', models.CharField(max_length=30)),
                ('thread1', models.CharField(max_length=60)),
                ('denim1', models.CharField(max_length=60)),
                ('cut1', models.CharField(max_length=30)),
                ('denim2', models.CharField(max_length=60)),
                ('thread2', models.CharField(max_length=60)),
                ('cut2', models.CharField(max_length=30)),
                ('prevMeasurement', models.CharField(max_length=30)),
                ('tailorId', models.CharField(max_length=30)),
                ('dateOfMeasurement', models.CharField(max_length=30)),
                ('timeOfMeasurement', models.CharField(max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
