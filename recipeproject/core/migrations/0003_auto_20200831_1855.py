# Generated by Django 3.1 on 2020-08-31 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_delete_usermanager'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
