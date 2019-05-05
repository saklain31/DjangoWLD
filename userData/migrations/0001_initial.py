# Generated by Django 2.2.1 on 2019-05-05 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tempOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderID', models.CharField(max_length=30)),
                ('userID', models.CharField(max_length=30)),
                ('gmail', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=30)),
                ('zipcode', models.CharField(max_length=30)),
                ('jeans1_1', models.CharField(max_length=60)),
                ('jeans1_2', models.CharField(max_length=60)),
                ('jeans1_3', models.CharField(max_length=30)),
                ('jeans2_1', models.CharField(max_length=60)),
                ('jeans2_2', models.CharField(max_length=60)),
                ('jeans2_3', models.CharField(max_length=30)),
            ],
        ),
    ]