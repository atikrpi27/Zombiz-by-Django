# Generated by Django 4.0.1 on 2022-02-01 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_registration_district_registration_gender_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='first_name',
            field=models.CharField(blank='True', max_length=20, null='True'),
        ),
        migrations.AlterField(
            model_name='registration',
            name='last_name',
            field=models.CharField(blank='True', max_length=20, null='True'),
        ),
        migrations.AlterField(
            model_name='registration',
            name='phone',
            field=models.IntegerField(blank='True', null='True'),
        ),
    ]
