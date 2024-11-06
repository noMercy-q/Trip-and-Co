SELECT 'CREATE DATABASE hac_db'
WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'hac_db');
\c hac_db


CREATE TABLE IF NOT EXISTS cities (
    city_id VARCHAR(10) PRIMARY KEY,
    city_name VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS airports (
    airport_id VARCHAR(10) PRIMARY KEY,
    airport_name VARCHAR(100),
    city_id VARCHAR(10),
    FOREIGN KEY (city_id) REFERENCES cities(city_id)
);

COPY cities FROM '/docker-entrypoint-initdb.d/data/cities.csv' DELIMITER ',' CSV HEADER;
COPY airports FROM '/docker-entrypoint-initdb.d/data/airports.csv' DELIMITER ',' CSV HEADER;