# Generated by Django 5.0.6 on 2024-12-03 21:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0002_appointment'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Dogs',
            new_name='Dog',
        ),
    ]
