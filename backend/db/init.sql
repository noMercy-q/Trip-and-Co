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

CREATE TABLE IF NOT EXISTS users (
    id uuid PRIMARY KEY default gen_random_uuid(),
    name VARCHAR,
    email VARCHAR unique,
    password_hash VARCHAR,
    created_at TIMESTAMPTZ default now()
);

COPY cities FROM '/docker-entrypoint-initdb.d/data/cities.csv' DELIMITER ',' CSV HEADER;
COPY airports FROM '/docker-entrypoint-initdb.d/data/airports.csv' DELIMITER ',' CSV HEADER;
COPY users FROM '/docker-entrypoint-initdb.d/data/users.csv' DELIMITER ',' CSV HEADER;


CREATE TABLE IF NOT EXISTS trips (
    id SERIAL PRIMARY KEY,
    name VARCHAR,
    description TEXT,
    origin_city_id VARCHAR,
    dest_city_id VARCHAR,
    created_by UUID,
    start_date TIMESTAMPTZ,
    end_date TIMESTAMPTZ,
    created_at TIMESTAMPTZ,
    invite_token VARCHAR,
    FOREIGN KEY (created_by) REFERENCES users(id),
    FOREIGN KEY (origin_city_id) REFERENCES cities(city_id),
    FOREIGN KEY (dest_city_id) REFERENCES cities(city_id)
);

DROP TYPE IF EXISTS UserRole;
CREATE TYPE UserRole AS ENUM ('owner', 'user');

CREATE TABLE IF NOT EXISTS trip_participants (
    id SERIAL PRIMARY KEY,
    trip_id INT,
    user_id UUID,
    role UserRole,
    joined_at TIMESTAMPTZ,
    FOREIGN KEY (trip_id) REFERENCES trips(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

DROP TYPE IF EXISTS TripItemsTypes;
CREATE TYPE TripItemsTypes AS ENUM ('hotel', 'vehicle', 'view');

CREATE TABLE IF NOT EXISTS trip_items (
    id SERIAL PRIMARY KEY,
    type TripItemsTypes,
    trip_id INT,
    name VARCHAR,
    description TEXT,
    details JSON,
    cost DECIMAL,
    image_url TEXT,
    link_url TEXT
);

CREATE TABLE IF NOT EXISTS votes (
    id SERIAL PRIMARY KEY,
    user_id UUID,
    trip_item_id INT,
    created_at TIMESTAMPTZ,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (trip_item_id) REFERENCES trip_items(id)
);

CREATE TABLE IF NOT EXISTS comments (
    id SERIAL PRIMARY KEY,
    user_id UUID,
    trip_item_id INT,
    content TEXT,
    created_at TIMESTAMPTZ,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (trip_item_id) REFERENCES trip_items(id)
);

CREATE TABLE IF NOT EXISTS trip_participants (
    id SERIAL PRIMARY KEY,
    user_id UUID,
    trip_id INT,
    joined_at TIMESTAMPTZ default now(),
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (trip_id) REFERENCES trips(id)
);
