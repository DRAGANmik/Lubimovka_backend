# Generated by Django 3.2.13 on 2022-06-16 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0019_auto_20220616_1613'),
    ]

    operations = [
        migrations.RenameField(
            model_name='festival',
            old_name='press_release_image',
            new_name='festival_image',
        ),
    ]
