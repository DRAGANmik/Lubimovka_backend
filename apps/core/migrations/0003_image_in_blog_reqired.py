# Generated by Django 3.2.11 on 2022-01-30 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_setting_initial_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='image',
            field=models.ImageField(blank=True, help_text='Обязательно указать для: членов команды, попечителей фестиваля и волонтёров.', upload_to='images/person_avatars', verbose_name='Фотография'),
        ),
    ]