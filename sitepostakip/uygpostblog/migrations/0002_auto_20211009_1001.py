# Generated by Django 3.0.6 on 2021-10-09 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uygpostblog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiller',
            name='Bit_Tarihi',
            field=models.DateTimeField(default='2050-01-01 00:00:00'),
        ),
    ]