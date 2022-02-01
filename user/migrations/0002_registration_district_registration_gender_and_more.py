# Generated by Django 4.0.1 on 2022-02-01 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='district',
            field=models.CharField(blank='False', max_length=30, null='False'),
            preserve_default='False',
        ),
        migrations.AddField(
            model_name='registration',
            name='gender',
            field=models.CharField(blank='False', max_length=20, null='False'),
            preserve_default='False',
        ),
        migrations.AddField(
            model_name='registration',
            name='username',
            field=models.CharField(blank='False', max_length=10, null='False'),
            preserve_default='False',
        ),
        migrations.AlterField(
            model_name='registration',
            name='email',
            field=models.EmailField(blank='False', max_length=30, null='False'),
        ),
    ]