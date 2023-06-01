## Places-Remember
Веб-приложение, с помощью которого люди смогут хранить свои впечатления о посещаемых
местах.


### Что не удалось сделать(сроки)
- Покрытие юнит-тестами.
### Планы по доработке и развитию приложения
- Покрыть юнит-тестами.
- Вход в систему реализовать с помощью других социальных сетей.
- Запуск тестов при новых коммитах реализовать с использованием CI/CD (github actions).
- Добавить возможность места разделять по группам.
- Запустить проект на одном из облачных сервисов.


#### Запуск проекта в docker контейнере

- Клонирование удаленного репозитория
```bash
git clone git@github.com:Zhuravlev-DP/Places-Remember.git
cd places_remember/
```
- В директории places_remember/ выполните сборку образа
```bash
docker build -t places_remember .
```
- Далее выполните запуск контейнера
```bash
docker run --name places_remember -it -p 8000:8000 places_remember
```
- В новом терминале выполните команду
```bash
docker container ls
```
- По полученному CONTAINER ID попадаем в оболочку запущенного контейнера
```bash
docker exec -t -i <CONTAINER ID> bash
```
- Выполните миграции, создайте суперпользователя
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```
- Стандартная админ-панель Django доступна по адресу [`http://localhost:8000/admin/`](http://localhost:8000/admin/)
- Проекту доступна по адресу [`http://localhost:8000/`](http://localhost:8000/)

#### Запуск проекта в dev-режиме

- Клонирование удаленного репозитория (см. выше)
- Создание виртуального окружения и установка зависимостей
```bash
cd places_remember
python -m venv venv
. venv/Scripts/activate (windows)
. venv/bin/activate (linux)
pip install --upgade pip
pip install -r -requirements.txt
```
- Примените миграции, создайте суперпользователя
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```
- Запуск сервера
```bash
python manage.py runserver
```