# <img src="https://raw.githubusercontent.com/4byra6ka/HappyBirthday/0fe1df9c77c145c01046a835d7c213b128aa0918/static/HappyBirthday.svg" width="89"/>

## Django проект "Сервис для поздравлений с днем рождения"

#### В проекте реализована рассылка оповещений сотрудников о предстоящем дне рождения именинника.
***
#### Реализованы цели:
* Цель удобное поздравление сотрудников.
* Получения списка сотрудников прямая регистрация. Только модератор может добавлять сотрудников(отметить is_staff можно в "Редактирование профиля") или при регистрации сотрудник автомотически добавится в список. 
* Авторизация.
* Возможность подписаться и отписаться от оповещения о дне рождения.
* Оповещение о ДР того на кого подписан.
* Внешнее взаимодействие фронт.
* Настройка времени оповещения до дня рождения на почту.

***
### Прежде чем начать использовать проект нужно:
* Установить PostgreSQL на сервер или ПК и предварительно настроить БД.
* Установить БД Redis `sudo apt install redis`.
* Создать файл `.evn` для передачи личных данных в Django настройки.


    EMAIL_HOST_USER=<Почта>
    EMAIL_HOST_PASSWORD=<Пароль>
    ALLOWED_HOSTS=<*>
    LANGUAGE_CODE=<ru-ru>
    TIME_ZONE=<Europe/Moscow>
    POSTGRES_DB=<Имя базы данны>
    POSTGRES_USER=<Пользователь в БД>
    POSTGRES_PASSWORD=<Пароль до БД>
    DATABASES_HOST=<xx.xx.xx.xx>
    DEBUG=<True/False>
    CELERY_BROKER_URL=<redis://xx.xx.xx.xx:6379>
    CELERY_RESULT_BACKEND=<redis://xx.xx.xx.xx:6379>
    CSRF_TRUSTED_ORIGINS=<Доверенные имена указать через ,>


### Разворачивание проекта "Сервис для поздравлений с днем рождения"


    git clone https://github.com/4byra6ka/HappyBirthday.git
    cd HappyBirthday
    poetry install
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver <IP>:<PORT>
    celery -A config worker -l INFO
    celery -A config beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler


***
### Также можно запустить через Docker:
* Нужно подправить файл `.evn.dev` и поля `EMAIL_HOST_USER`,`EMAIL_HOST_PASSWORD`,`CSRF_TRUSTED_ORIGINS`.


    EMAIL_HOST_USER=<Почта>
    EMAIL_HOST_PASSWORD=<Пароль>
    ALLOWED_HOSTS=*
    LANGUAGE_CODE=ru-ru
    TIME_ZONE=Europe/Moscow
    POSTGRES_DB=happy_birthday
    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=postgres
    DATABASES_HOST=db
    DEBUG=True
    CELERY_BROKER_URL=redis://redis:6379/0
    CELERY_RESULT_BACKEND=redis://redis:6379/0
    CSRF_TRUSTED_ORIGINS=https://proxy,http://proxy:8080

### Разворачивание проекта "Сервис для поздравлений с днем рождения" через docker
    git clone https://github.com/4byra6ka/HappyBirthday.git
    cd HappyBirthday
    poetry install
    docker-compose build
    docker-compose up

PS: Можно протестировать сайт [здесь](https://vpn.1jz.ru) 
