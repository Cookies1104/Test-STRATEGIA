# Тестовое задание API.
Функциональные требования:

У системы должны быть методы API, которые обеспечивают
- Добавление статьи (Можно чисто номинально, как сущность, к которой крепятся комментарии).
- Добавление комментария к статье.
- Добавление коментария в ответ на другой комментарий (возможна любая вложенность).
- Получение всех комментариев к статье вплоть до 3 уровня вложенности.
- Получение всех вложенных комментариев для комментария 3 уровня.
- По ответу API комментариев можно воссоздать древовидную структуру.

Нефункциональные требования:
- Использование Django ORM.
- Следование принципам REST.
- Число запросов к базе данных не должно напрямую зависеть от количества комментариев, уровня вложенности.
- Решение в виде репозитория на Github, Gitlab или Bitbucket.
- readme, в котором указано, как собирать и запускать проект. Зависимости указать в requirements.txt либо использовать poetry/pipenv.
- Использование свежих версий python и Django.

Будет плюсом:
- Использование PostgreSQL.
- docker-compose для запуска api и базы данных.
- Swagger либо иная документация к апи.

Всё остальное (авторизация, админки, тесты) - по желанию, оцениваться не будет. Использование DRF не обязательно.

Запуск контейнера в режиме docker-compose
1. Создайте каталог для запуска образа в режиме docker-compose
2. Создайте файл docker-compose.yml в созданном каталоге с приведённом ниже кодом, заполнив данные о БД своими значенями

```
version: '3.8'

services:
  web:
    image: cookies1104/project_1:test_1
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - web:/usr/src/app/
    ports:
      - 8000:8000
    env_file:
      - ./env.dev
  db:
    image: postgres:14.0-alpine
    volumes:
      - postgres_data:/var/lib/postgresql/data/
    environment:
      - POSTGRES_USER=<Your user>
      - POSTGRES_PASSWORD=<Your pass>
      - POSTGRES_DB=<Your db>

volumes:
  web:
  postgres_data:
```
Если TCP-порт 8000 занят укажите любой другой свободный порт.

3. Создайте файл env.dev в каталоге с файлом docker-compose.yml с приведённым ниже кодом, также заполнив данные о БД своими значениями:
```
DEBUG=1
SECRET_KEY=foo
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=<Your db>
SQL_USER=<Your user>
SQL_PASSWORD=<Your pass>
SQL_HOST=db
SQL_PORT=5432
DATABASE=postgres
```
4. Перейдите в созданный каталог и запустите команду:
```
docker-compose up -d
```
5. Запустите миграцию командой:
```
docker-compose exec web python manage.py migrate --noinput
```
6. Запустите страницу http://localhost:8000/api/swagger-ui/ с документацией Swagger к API указав, при необходимости, вместо 8000 порт с файла docker-compose.yml 

