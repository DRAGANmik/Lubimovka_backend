# Generated by Django 3.2.11 on 2022-01-29 14:40

import apps.core.validators
from django.db import migrations, models


def create_roles(apps, schema_editor):
    Role = apps.get_model("core", "Role")
    roles = [
        {
            "name": "Актёр",
            "name_plural": "Актёры",
            "slug": "actor",
        },
        {
            "name": "Адаптация текста",
            "name_plural": "Адаптация текста",
            "slug": "text_adaptation",
        },
        {
            "name": "Драматург",
            "name_plural": "Драматурги",
            "slug": "dramatist",
        },
        {
            "name": "Режиссёр",
            "name_plural": "Режиссёры",
            "slug": "director",
        },
        {
            "name": "Переводчик",
            "name_plural": "Переводчики",
            "slug": "translator",
        },
        {
            "name": "Ведущий",
            "name_plural": "Ведущие",
            "slug": "host",
        },
        {
            "name": "Текст",
            "name_plural": "Текст",
            "slug": "text",
        },
        {
            "name": "Иллюстрации",
            "name_plural": "Иллюстрации",
            "slug": "illustrations",
        },
        {
            "name": "Фото",
            "name_plural": "Фото",
            "slug": "photo",
        },
    ]
    for role in roles:
        role_obj, _ = Role.objects.get_or_create(**role)
        role_obj.save()

def create_role_types(apps, schema_editor):
    RoleType = apps.get_model("core", "RoleType")
    role_types = [
        {
            "role_type": "blog_persons_role",
        },
        {
            "role_type": "performanse_role",
        },
        {
            "role_type": "play_role",
        },
        {
            "role_type": "master_class_role",
        },
        {
            "role_type": "reading_role",
        },
    ]
    for type in role_types:
        type_obj, _ = RoleType.objects.get_or_create(**type)
        type_obj.save()

def add_types_to_roles(apps, schema_editor):
    Role = apps.get_model("core", "Role")
    RoleType = apps.get_model("core", "RoleType")
    roles = [
        {
            "name": "Актёр",
            "slug": "actor",
            "types": "performanse_role",
        },
        {
            "name": "Адаптация текста",
            "slug": "text_adaptation",
            "types": "blog_persons_role",
        },
        {
            "name": "Драматург",
            "slug": "dramatist",
            "types": "play_role",
        },
        {
            "name": "Драматург",
            "slug": "dramatist",
            "types": "performanse_role",
        },
        {
            "name": "Драматург",
            "slug": "dramatist",
            "types": "reading_role",
        },
        {
            "name": "Режиссёр",
            "slug": "director",
            "types": "performanse_role",
        },
        {
            "name": "Режиссёр",
            "slug": "director",
            "types": "reading_role",
        },
        {
            "name": "Переводчик",
            "slug": "translator",
            "types": "blog_persons_role",
        },
        {
            "name": "Ведущий",
            "slug": "host",
            "types": "play_role",
        },
        {
            "name": "Ведущий",
            "slug": "host",
            "types": "master_class_role",
        },
        {
            "name": "Текст",
            "slug": "text",
            "types": "blog_persons_role",
        },
        {
            "name": "Иллюстрации",
            "slug": "illustrations",
            "types": "blog_persons_role",
        },
        {
            "name": "Фото",
            "slug": "photo",
            "types": "blog_persons_role",
        },
    ]
    for role in roles:
        role_obj = Role.objects.get(name=role["name"])
        type_of_role = RoleType.objects.get(role_type=role["types"])
        role_obj.types.add(type_of_role)
        role_obj.save()

def add_settings(apps, schema_editor):
    Settings = apps.get_model('core', 'Settings')
    '''
    Settings.objects.create(
        field_type="BOOLEAN",
        settings_key="festival_status",
        boolean=True,
        description="Статус фестиваля",
    )
    Settings.objects.create(
        field_type="TEXT",
        settings_key="site_color",
        text="green",
        description="Цвет сайта",
    )
    Settings.objects.create(
        field_type="BOOLEAN",
        settings_key="form_to_submit_a_play",
        boolean=True,
        description="Форма для отправки пьесы",
    )
    Settings.objects.create(
        field_type="TEXT",
        settings_key="email_subject_for_question",
        text="Вопрос Любимовке",
        description="Тема письма для вопроса",
    )

def do_some():
    # for what is this? -->>>
    values = [
        "Festival_status",
        "Site_color",
        "Mail_send_to",
        "Form_to_submit_a_play"
    ]
    for value in values:
        if Settings.objects.filter(
            settings_key=value,
        ).exists():
            setting = Settings.objects.get(settings_key=value,)
            setting.settings_key = value.lower()
            setting.save()
    # <<<--

    Settings.objects.create(
        field_type="BOOLEAN",
        settings_key="main_add_afisha",
        boolean=True,
        description="Отображение афиши на главной страницы",
    )
    Settings.objects.create(
        field_type="BOOLEAN",
        settings_key="main_show_afisha_only_for_today",
        boolean=True,
        description="Отображение афиши только на сегодня (в противном случае " "на ближайшие 6 дней)",
    )
    Settings.objects.create(
        field_type="BOOLEAN",
        settings_key="main_add_news",
        boolean=True,
        description="Отображение новостей на главной страницы",
    )
    Settings.objects.create(
        field_type="TEXT",
        settings_key="main_news_title",
        text="Новости",
        description="Заголовок для новостей на главной страницы",
    )
    Settings.objects.create(
        field_type="BOOLEAN",
        settings_key="main_add_blog",
        boolean=True,
        description="Отображение дневника на главной страницы",
    )
    Settings.objects.create(
        field_type="TEXT",
        settings_key="main_blog_title",
        text="Дневник фестиваля",
        description="Заголовок для дневника на главной страницы",
    )
    Settings.objects.create(
        field_type="BOOLEAN",
        settings_key="main_add_banners",
        boolean=True,
        description="Отображение банера на главной страницы",
    )
    Settings.objects.create(
        field_type="BOOLEAN",
        settings_key="main_add_short_list",
        boolean=True,
        description="Отображение шорт-листа на главной страницы",
    )
    Settings.objects.create(
        field_type="TEXT",
        settings_key="main_short_list_title",
        text="Шорт-лист 2020 года",
        description="Заголовок для шорт-листа на главной страницы",
    )
    Settings.objects.create(
        field_type="BOOLEAN",
        settings_key="main_add_video_archive",
        boolean=True,
        description="Отображение видео-архива на главной страницы",
    )
    Settings.objects.create(
        field_type="URL",
        settings_key="main_video_archive_url",
        url="https://lubimovks.url.ru",
        description="Ссылка на youtube видео-архива на главной страницы",
    )
    Settings.objects.create(
        field_type="IMAGE",
        settings_key="main_video_archive_photo",
        image="core/2021-09-30_14.37.56.jpg",
        description="Фото для видео-архива на главной страницы",
    )
    Settings.objects.create(
        field_type="BOOLEAN",
        settings_key="main_add_places",
        boolean=True,
        description="Отображение площадок на главной страницы",
    )
    Settings.objects.create(
        field_type="BOOLEAN",
        settings_key="main_add_first_screen",
        boolean=True,
        description="Отображение первой страницы",
    )
    Settings.objects.create(
        field_type="TEXT",
        settings_key="main_first_screen_title",
        text="Открыт прием пьес на фестиваль 2021 года",
        description="Заголовок для первой страницы",
    )
    Settings.objects.create(
        field_type="TEXT",
        settings_key="main_first_screen_url_title",
        text="Заголовок для ссылки для первой страницы",
        description="Заголовок для первой страницы",
    )
    Settings.objects.create(
        field_type="URL",
        settings_key="main_first_screen_url",
        url="https://lubimovks.url.ru",
        description="Ссылка для первой страницы страницы",
    )

def sort_by_group(apps, schema_editor):
    Setting = apps.get_model('core', 'Setting')
    group = {
        "EMAIL": "mail",
        "MAIN": "main",
        "FIRST_SCREEN": "first_screen",
        "GENERAL": "GENERAL"
    }
    setting_first_screen = Setting.objects.filter(
        settings_key__icontains=group['FIRST_SCREEN']
    ).all()
    for setting in setting_first_screen:
        setting.group = 'FIRST_SCREEN'
        setting.save()
    setting_main = Setting.objects.filter(
        settings_key__icontains=group['MAIN'],
        group='GENERAL'
    ).all()
    for setting in setting_main:
        setting.group = 'MAIN'
        setting.save()
    setting_email = Setting.objects.filter(
        settings_key__icontains=group['EMAIL'],
        group="GENERAL"
    ).all()
    for setting in setting_email:
        setting.group = 'EMAIL'
        setting.save()

def add_settings_2(apps, schema_editor):

    Setting = apps.get_model("core", "Setting")

    Setting.objects.create(
        field_type="TEXT",
        group="EMAIL",
        settings_key="email_question_template_id",
        text="3420599",
        description="Id шаблона письма с вопросом",
    )
    Setting.objects.create(
        field_type="TEXT",
        group="EMAIL",
        settings_key="email_send_from",
        text="questions@lyubimovka.ru",
        description="Почта для отправки вопроса",
    )
    Setting.objects.create(
        field_type="TEXT",
        group="EMAIL",
        settings_key="email_send_to",
        text="admin@lyubimovka.ru",
        description="Почта для приёма вопроса",
    )

def add_afisha_and_first_screen_settings(apps, schema_editor):
    Setting = apps.get_model("core", "Setting")
    Setting.objects.create(
        field_type="TEXT",
        group="AFISHA",
        settings_key="afisha_title_festival",
        text="Афиша фестиваля",
        description="Заголовок афиши во время фестиваля",
    )
    Setting.objects.create(
        field_type="TEXT",
        group="AFISHA",
        settings_key="afisha_title_regular",
        text="Афиша событий",
        description="Заголовок афиши регулярный",
    )
    Setting.objects.create(
        field_type="TEXT",
        group="AFISHA",
        settings_key="afisha_description_festival",
        text="На все читки и мастер-классы фестиваля вход свободный по предварительной регистрации.",
        description="Описание под заголовком во время фестиваля",
    )
    Setting.objects.create(
        field_type="TEXT",
        group="AFISHA",
        settings_key="afisha_description_regular",
        text="На все читки и мастер-классы фестиваля вход свободный по предварительной регистрации.",
        description="Описание под заголовком регулярное",
    )
    Setting.objects.create(
        field_type="TEXT",
        group="AFISHA",
        settings_key="afisha_info_festival_text",
        text="Регистрация на каждое мероприятие открывается в 12:00 предыдущего дня.",
        description="Информация о регистрации на событие фестиваля",
    )
    Setting.objects.create(
        field_type="TEXT",
        group="AFISHA",
        settings_key="afisha_asterisk_text",
        text="После каждой читки будет проходить обсуждение с участием аудитории, автора и театральных профессионалов.",
        description="Текст со звёздочкой возле заголовка",
    )
    Setting.objects.create(
        field_type="IMAGE",
        group="FIRST_SCREEN",
        settings_key="main_first_screen_image",
        image="core/2021-09-30_14.37.56.jpg",
        description="Изображение для первой страницы",
    )
'''

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(help_text='Загрузите фотографию', upload_to='images/', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Изображения',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=50, validators=[apps.core.validators.name_validator], verbose_name='Имя')),
                ('last_name', models.CharField(max_length=50, validators=[apps.core.validators.name_validator], verbose_name='Фамилия')),
                ('middle_name', models.CharField(blank=True, max_length=50, validators=[apps.core.validators.name_validator], verbose_name='Отчество')),
                ('city', models.CharField(blank=True, help_text='Обязательно указать для: членов команды, волонтёров и авторов.', max_length=50, verbose_name='Город проживания')),
                ('email', models.EmailField(blank=True, help_text='Обязательно указать для: членов команды, волонтёров и авторов.', max_length=200, null=True, unique=True, verbose_name='Электронная почта')),
                ('image', models.ImageField(blank=True, help_text='Обязательно указать для: членов команды, спонсоров и волонтёров.', upload_to='images/person_avatars', verbose_name='Фотография')),
            ],
            options={
                'verbose_name': 'Человек',
                'verbose_name_plural': 'Люди',
                'ordering': ('last_name',),
            },
        ),
        migrations.CreateModel(
            name='RoleType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_type', models.CharField(choices=[('blog_persons_role', 'Роль в блоге'), ('performanse_role', 'Роль в спектаклях'), ('play_role', 'Роль в пьесах'), ('master_class_role', 'Роль в мастер классах'), ('reading_role', 'Роль в читках')], default='blog_persons_role', help_text='Укажите, где будет использована роль', max_length=20, unique=True, verbose_name='Тип роли')),
            ],
            options={
                'verbose_name': 'Тип роли',
                'verbose_name_plural': 'Типы ролей',
            },
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('group', models.CharField(choices=[('EMAIL', 'Почта'), ('MAIN', 'Главная'), ('FIRST_SCREEN', 'Первая страница'), ('GENERAL', 'Общие'), ('AFISHA', 'Афиша')], default='GENERAL', max_length=50, verbose_name='Группа настроек')),
                ('field_type', models.CharField(choices=[('BOOLEAN', 'Да/Нет'), ('TEXT', 'Текст'), ('URL', 'URL'), ('IMAGE', 'Картинка'), ('EMAIL', 'EMAIL')], max_length=40, verbose_name='Выбор поля настроек')),
                ('settings_key', models.SlugField(max_length=40, unique=True, verbose_name='Ключ настройки')),
                ('description', models.TextField(blank=True, max_length=250, verbose_name='Описание настройки')),
                ('boolean', models.BooleanField(default=False, verbose_name='Да или Нет')),
                ('text', models.TextField(blank=True, max_length=500, verbose_name='Текст')),
                ('url', models.URLField(blank=True, verbose_name='Ссылка')),
                ('image', models.ImageField(blank=True, upload_to='core/', verbose_name='Изображение')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Email')),
            ],
            options={
                'verbose_name': 'Общие настройки',
                'verbose_name_plural': 'Общие настройки',
                'ordering': ('group', 'settings_key'),
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Название')),
                ('name_plural', models.CharField(max_length=50, unique=True, verbose_name='Название во множественном числе')),
                ('slug', models.SlugField(help_text='Если пустое, то заполняется автоматически', max_length=60, unique=True, verbose_name='Код-имя латиницей')),
                ('types', models.ManyToManyField(related_name='type_roles', to='core.RoleType', verbose_name='Типы ролей')),
            ],
            options={
                'verbose_name': 'Должность/позиция',
                'verbose_name_plural': 'Должности/позиции',
                'ordering': ('name',),
            },
        ),
        migrations.AddConstraint(
            model_name='person',
            constraint=models.UniqueConstraint(fields=('first_name', 'last_name', 'middle_name', 'email'), name='unique_person'),
        ),
        migrations.RunPython(
            create_roles,
            create_role_types,
            add_types_to_roles,
            add_settings,
        )
    ]
