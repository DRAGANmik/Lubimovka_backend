# Generated by Django 3.2.11 on 2022-01-29 14:40

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models

import apps.content_pages.utilities


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(max_length=500, verbose_name='Описание')),
                ('image', models.ImageField(blank=True, upload_to=apps.content_pages.utilities.path_by_app_label_and_class_name, verbose_name='Заглавная картинка')),
                ('is_draft', models.BooleanField(default=True, help_text='Поставьте отметку если это черновик', verbose_name='Черновик')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата публикации')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('author_url', models.URLField(verbose_name='Ссылка на автора записи')),
                ('author_url_title', models.CharField(max_length=50, verbose_name='Подпись/название ссылки на автора')),
            ],
            options={
                'verbose_name': 'Запись блога',
                'verbose_name_plural': 'Блог',
                'ordering': ('-pub_date',),
            },
        ),
        migrations.CreateModel(
            name='NewsItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(max_length=500, verbose_name='Описание')),
                ('image', models.ImageField(blank=True, upload_to=apps.content_pages.utilities.path_by_app_label_and_class_name, verbose_name='Заглавная картинка')),
                ('is_draft', models.BooleanField(default=True, help_text='Поставьте отметку если это черновик', verbose_name='Черновик')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата публикации')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
                'ordering': ('-pub_date',),
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(max_length=500, verbose_name='Описание')),
                ('is_draft', models.BooleanField(default=True, help_text='Поставьте отметку если это черновик', verbose_name='Черновик')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата публикации')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('image', models.ImageField(upload_to='images/articles/projects/', verbose_name='Заглавная картинка')),
                ('intro', models.TextField(help_text='Короткое интро к проекту. Показывается в списке проектов с заголовком.', max_length=200, verbose_name='Интро к проекту')),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проекты',
                'ordering': ('-pub_date',),
            },
        ),
        migrations.CreateModel(
            name='ProjectContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField(verbose_name='ID объекта')),
                ('order', models.PositiveSmallIntegerField(default=0, verbose_name='Порядок')),
                ('content_page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contents', to='articles.project', verbose_name='Проект с конструктором')),
                ('content_type', models.ForeignKey(limit_choices_to={'app_label': 'content_pages'}, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype', verbose_name='Тип объекта')),
            ],
            options={
                'verbose_name': 'Блок/элемент конструктора проекта',
                'verbose_name_plural': 'Блоки/элементы конструктора проектов',
                'ordering': ('order',),
            },
        ),
        migrations.CreateModel(
            name='NewsItemContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField(verbose_name='ID объекта')),
                ('order', models.PositiveSmallIntegerField(default=0, verbose_name='Порядок')),
                ('content_page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contents', to='articles.newsitem', verbose_name='Запись блога с конструктором')),
                ('content_type', models.ForeignKey(limit_choices_to={'app_label': 'content_pages'}, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype', verbose_name='Тип объекта')),
            ],
            options={
                'verbose_name': 'Блок/элемент конструктора новости',
                'verbose_name_plural': 'Блоки/элементы конструктора новостей',
                'ordering': ('order',),
            },
        ),
        migrations.CreateModel(
            name='BlogPerson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_persons', to='articles.blogitem', verbose_name='Блог')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='blog_persons', to='core.person', verbose_name='Соавтор блога')),
                ('role', models.ForeignKey(limit_choices_to={'types__role_type': 'blog_persons_role'}, on_delete=django.db.models.deletion.RESTRICT, related_name='blog_persons', to='core.role', verbose_name='Роль в соавторстве')),
            ],
            options={
                'verbose_name': 'Соавтор блога',
                'verbose_name_plural': 'Соавторы блогов',
                'ordering': ('role',),
            },
        ),
        migrations.CreateModel(
            name='BlogItemContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField(verbose_name='ID объекта')),
                ('order', models.PositiveSmallIntegerField(default=0, verbose_name='Порядок')),
                ('content_page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contents', to='articles.blogitem', verbose_name='Запись блога с конструктором')),
                ('content_type', models.ForeignKey(limit_choices_to={'app_label': 'content_pages'}, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype', verbose_name='Тип объекта')),
            ],
            options={
                'verbose_name': 'Блок/элемент конструктора записи блога',
                'verbose_name_plural': 'Блоки/элементы конструктора записей блога',
                'ordering': ('order',),
            },
        ),
        migrations.AddField(
            model_name='blogitem',
            name='roles',
            field=models.ManyToManyField(related_name='blogs', through='articles.BlogPerson', to='core.Role', verbose_name='Роли'),
        ),
        migrations.AddConstraint(
            model_name='blogperson',
            constraint=models.UniqueConstraint(fields=('person', 'blog', 'role'), name='unique_person_role_per_blog'),
        ),
    ]
