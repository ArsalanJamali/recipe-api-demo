# Generated by Django 3.1 on 2020-10-01 14:00

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_recipe'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=core.models.recipe_image_file_path),
        ),
    ]
