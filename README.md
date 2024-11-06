### Установка зависимостей и запуск frontend
```bash
cd ./frontend
npm install
npm run serve # По умолчанию поднимается на 8080 порту
```

## Backend
### Установка зависимостей
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Локальный запуск postgresql
```shell
backend/postgres_run.sh
```

To connect via psql to local postgres:
```shell
docker exec -it postgres psql -U postgres -d hac_db
```

Структура базы данных: https://dbdiagram.io/d/672b9adee9daa85aca8c62b7


### Структура проекта 
├── api_clients
│   └── aviasales_client.py
├── app
│    ├── __init__.py
│    ├── routes
│    │       └── *.py
│    └── services
│        └── *.py
├── db
│    ├── client.py
│    ├── data
│    │   ├── *.csv
│    │
│    ├── init.sql
│    └── models.py
├── main.py
└── postgres_run.sh

main.py - основная настройка приложения без инициализации каких-либо других клиентов

api_clients/ - клиенты для взаимодействия с внешним API

app/__init__.py - инициализация глобальных объектов(коннект к базе, клиент авиа, etc) и импорт всех нужных модулей

app/routes/ - для маршрутов и хендлеров

app/services/ - "сервисы" для реализации бизнес логики (которые могут использовать внешних клиентов), например для avia 
это сервис для обработки данных в нужный формат, чтобы отдать на фронт