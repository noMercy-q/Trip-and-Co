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


### Создание тестовых данных 
/create_trip
```bash
curl -i http://0.0.0.0:8000/create_trip -d '{"name": "test-trip", "origin_city_id": "MOW", "dest_city_id": "DXB", "created_by": "38171859-980f-438b-b220-be0e4bc9d631", "start_date": "2024-11-30", "end_date": "2024-12-25"}' -X POST -H "Content-Type: application/json"
```

/create_view
```bash
curl -i http://0.0.0.0:8000/create_view  -X POST -H "Content-Type: application/json" -d '{"name": "test-trip-item", "trip_id": "1", "type": "hotel"}'
```

/create_vote
```bash
curl -i http://0.0.0.0:8000/votes  -X POST -H "Content-Type: application/json" -d '{"trip_item_id": "1", "user": "38171859-980f-438b-b220-be0e4bc9d631"}'
```