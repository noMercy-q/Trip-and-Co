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

CREATE TABLE IF NOT EXISTS users (
    id UUID PRIMARY KEY,
    name VARCHAR,
    email VARCHAR,
    password_hash VARCHAR,
    created_at TIMESTAMPTZ
);

CREATE TABLE IF NOT EXISTS trips (
    id UUID PRIMARY KEY,
    name VARCHAR,
    description TEXT,
    origin_city_id VARCHAR,
    dest_city_id VARCHAR,
    created_by UUID,
    start_date TIMESTAMPTZ,
    end_date TIMESTAMPTZ,
    created_at TIMESTAMPTZ,
    FOREIGN KEY (created_by) REFERENCES users(id),
    FOREIGN KEY (origin_city_id) REFERENCES cities(city_id),
    FOREIGN KEY (dest_city_id) REFERENCES cities(city_id)
);

DROP TYPE IF EXISTS UserRole;
CREATE TYPE UserRole AS ENUM ('owner', 'user');

CREATE TABLE IF NOT EXISTS trip_participants (
    id UUID PRIMARY KEY,
    trip_id UUID,
    user_id UUID,
    role UserRole,
    joined_at TIMESTAMPTZ,
    FOREIGN KEY (trip_id) REFERENCES trips(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

DROP TYPE IF EXISTS TripItemsTypes;
CREATE TYPE TripItemsTypes AS ENUM ('hotels', 'vehicle', 'attraction');

CREATE TABLE IF NOT EXISTS trip_items (
    id UUID PRIMARY KEY,
    type TripItemsTypes,
    name VARCHAR,
    description TEXT,
    details JSON,
    cost DECIMAL
);

DROP TYPE IF EXISTS TargetType;
CREATE TYPE TargetType AS ENUM ('hotels', 'vehicle', 'attraction');

CREATE TABLE IF NOT EXISTS poll (
    id UUID PRIMARY KEY,
    type TargetType,
    trip_id UUID,
    FOREIGN KEY (trip_id) REFERENCES trips(id)
);

CREATE TABLE IF NOT EXISTS poll_options (
    id UUID PRIMARY KEY,
    poll_id UUID,
    trip_item_id UUID,
    created_at TIMESTAMPTZ,
    created_by UUID,
    FOREIGN KEY (poll_id) REFERENCES poll(id),
    FOREIGN KEY (trip_item_id) REFERENCES trip_items(id),
    FOREIGN KEY (created_by) REFERENCES users(id)
);

CREATE TABLE IF NOT EXISTS votes (
    id UUID PRIMARY KEY,
    user_id UUID,
    option_id UUID,
    created_at TIMESTAMPTZ,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (option_id) REFERENCES poll_options(id)
);

CREATE TABLE IF NOT EXISTS comments (
    id UUID PRIMARY KEY,
    user_id UUID,
    poll_option_id UUID,
    content TEXT,
    created_at TIMESTAMPTZ,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (poll_option_id) REFERENCES poll_options(id)
);
