# Generated by Django 4.2.1 on 2023-06-02 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='scheduled_for',
        ),
    ]
