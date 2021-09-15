# Бэкенд "Любимовка"

## Что сделано и чем отличается от структуры по умолчанию
- poetry как менеджер пакетов и управления зависимостями
- изменена структура:
    - настройки и django приложения в папке config
    - папка для приложений: apps
- отдельные настройки для тестов или локального / prod окружения
- базовые линтеры (black, flake8)
- pre-commit хуки
- используется PostgreSQL
- базовая модель TimeStampedModel (импортировать из core.models)
- djoser для эндпоинтов пользователя
- автодокументация swagger/redoc (http://base_url/api/schema/swagger-ui/ или http://base_url/api/schema/redoc/)

## Правила работы с git (как делать коммиты и pull request-ы)
**Не написано, ждёт когда кто-то напишет.**\
В планах придерживаться [вот таких](https://habr.com/ru/post/106912/) и [таких](https://www.atlassian.com/ru/git/tutorials/comparing-workflows/gitflow-workflow) схем

## Подготовка окружения для разработки

Что нужно подготовить предварительно:
1. **poetry** \
Зависимости и пакеты управляются через **poetry**. Детальное описание + как установить в [документации poetry](https://python-poetry.org/docs/cli/).
2. **Docker** \
Для разработки используется Postgres SQL. Базу данных удобно запускать через Docker.
3. Файлы **requirements** \
Файлы редактировать вручную не нужно. Обновляются через pre-commit хуки (если есть изменение в зависимостях, то список обновится при коммите).
4. **pre-commit хуки** \
[Документация](https://pre-commit.com)\
При каждом коммите выполняются хуки (автоматизации) перечисленные в **.pre-commit-config.yaml**. Если не понятно какая ошибка мешает сделать коммит можно запустить хуки вручную и посмотреть ошибки:
    ```shell
    pre-commit run --all-files
    ```

Если всё подготовлено:
1. Склонируйте проект, перейдите в папку backend
    ```shell
    git clone git@github.com:Studio-Yandex-Practicum/Lubimovka_backend.git
    cd Lubimovka_backend
    ```
2. Убедитесь что poetry установлен. Активируйте виртуальное окружение. Установите зависимости
    ```shell
    poetry shell
    poetry install
    ```
3. Установите pre-commit хуки
    ```shell
    pre-commit install --all
    ```
4. В IDE скорее всего потребуется указать путь до интерпретатора (скопируйте в IDE путь который вернет команда)
    ```shell
    poetry env info --path
    ```
5. Установить pre-commit хуки
    ```shell
    pre-commit install --all
    ```
6. Для запуска базы данных используйте postgres-local.yaml и docker-compose.
    ```
    docker-compose -f postgres-local.yaml up -d
    ```
7. Остановка, удаление и все остальные команды как с любым контейнером docker
    - Остановить контейнер с БД:
        ```shell
        docker-compose -f postgres-local.yaml down
        ```
    - Остановить контейнер с БД удалив данные:
        ```shell
        docker-compose -f postgres-local.yaml down --volumes
        ```
8. Локальные настройки не требуют переменных окружения. Если они потребуются:
    - раскоментируйте подключение **.env** в файле настроек **config.settings.local**
    - добавьте файл **.env** в корень папки проекта
## Про тесты

Тестов нет, но есть настройки для ускорения тестов + настройки для запуска unittest через pytest (удобно в vscode)