# Generated by Django 3.0.6 on 2020-07-06 06:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uygpostblog', '0004_takipler'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='takipler',
            name='isim',
        ),
    ]