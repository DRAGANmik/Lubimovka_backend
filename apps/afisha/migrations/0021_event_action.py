# Generated by Django 3.2.14 on 2022-09-05 17:35

from django.db import migrations, models


def move_paid_field_info(apps, schema_editor):
    Event = apps.get_model("afisha", "Event")
    Event.objects.filter(paid=True).update(action="TICKETS")

class Migration(migrations.Migration):

    dependencies = [
        ('afisha', '0020_auto_20220806_0111'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='action',
            field=models.CharField(choices=[('REGISTRATION', 'Регистрация'), ('TICKETS', 'Билеты'), ('STREAM', 'Трансляция')], default='REGISTRATION', help_text='Выберите название действия, соответсвующее содержанию ссылки', max_length=50, verbose_name='Название действия'),
        ),
        migrations.RunPython(move_paid_field_info),
        migrations.RemoveField(
            model_name='event',
            name='paid',
        )

    ]
