# Generated by Django 3.1 on 2020-10-01 06:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_ingredient'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['-pk']},
        ),
    ]