# Generated by Django 5.1 on 2024-08-11 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articles',
            name='date',
        ),
    ]
