# Generated by Django 3.1.4 on 2020-12-26 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('currency_exchange_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='user',
        ),
    ]