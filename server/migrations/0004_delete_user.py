# Generated by Django 5.0.6 on 2024-12-04 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0003_rename_dogs_dog'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
