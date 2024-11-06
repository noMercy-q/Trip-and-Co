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