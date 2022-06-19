# Generated by Django 3.2.13 on 2022-06-16 13:13

import apps.content_pages.utilities
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0018_auto_20220512_1432'),
    ]

    operations = [
        migrations.AddField(
            model_name='pressrelease',
            name='press_release_image',
            field=models.ImageField(blank=True, upload_to=apps.content_pages.utilities.path_by_app_label_and_class_name, verbose_name='Изображение для страницы пресс-релизов'),
        ),
        migrations.AlterField(
            model_name='festival',
            name='press_release_image',
            field=models.ImageField(blank=True, upload_to=apps.content_pages.utilities.path_by_app_label_and_class_name, verbose_name='Постер фестиваля'),
        ),
    ]
