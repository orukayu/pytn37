# Generated by Django 3.0.6 on 2020-06-15 11:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('uygpostblog', '0002_auto_20200529_2247'),
    ]

    operations = [
        migrations.AddField(
            model_name='talepler',
            name='tarih',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]