# Generated by Django 3.2.10 on 2022-01-13 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_alter_setting_group'),
        ('main', '0006_settingemail_settingfirstscreen_settinggeneral_settingmain'),
    ]

    operations = [
        migrations.CreateModel(
            name='SettingAfishaScreen',
            fields=[
            ],
            options={
                'verbose_name': 'Настройки афиши',
                'verbose_name_plural': 'Настройки афиши',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('core.setting',),
        ),
    ]
