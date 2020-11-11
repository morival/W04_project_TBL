DROP TABLE IF EXISTS sights;
DROP TABLE IF EXISTS cities;
DROP TABLE IF EXISTS countries;
DROP TABLE IF EXISTS continents;


CREATE TABLE continents (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE countries (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    continent_id INT REFERENCES continents(id) ON DELETE CASCADE,
    visited BOOLEAN
);

CREATE TABLE cities (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    country_id INT REFERENCES countries(id) ON DELETE CASCADE,
    visited BOOLEAN,
    comment TEXT
);

CREATE TABLE sights (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    city_id INT REFERENCES cities(id) ON DELETE CASCADE,
    visited BOOLEAN,
    comment TEXT
)