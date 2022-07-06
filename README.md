## _Рандомная картинка по запросу_

### Для установки: 

Использовался Python 3.10

#### Это для Windows:

* Создать виртуальную среду:

```
python -m venv venv
```

* Запустить виртуальную среду:

```
venv\Scripts\activate
```

* Скачать зависимости с requirements.txt:

```
pip install -r requirements.txt
```

* Создать файлик .env в корне проекта и в него положить некоторые переменные:

##### Обязательные: 

SECRET_KEY=

DEBUG_VALUE=

DJANGO_DEV=

##### Для базы данных postgreSQL:

DB_NAME=

DB_USER=

USER_PASSWORD=

DB_HOST=

DB_PORT=

* Запустить сервер:

```
python manage.py runserver
```

### Через Docker:

#### Добавить все переменные в docker-compose.yml

```
POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=

DB_NAME=
DB_USER=
USER_PASSWORD=
DB_HOST=
DB_PORT=
SECRET_KEY=
DEBUG_VALUE=
DJANGO_DEV=
```

### Запустить `docker-compose up` в директории проекта.
### И в конце, после запуска контейнера перейдите на http://localhost:8000/

### Скриншот главной страницы:
![](img/main_site.png)

### Json ответ:
![](img/json_response.png)
