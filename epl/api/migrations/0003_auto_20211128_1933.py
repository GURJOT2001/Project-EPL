# Generated by Django 3.2.9 on 2021-11-28 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20211127_2038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='email',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='first_name',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='last_name',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='password',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='username',
            field=models.CharField(max_length=10),
        ),
    ]