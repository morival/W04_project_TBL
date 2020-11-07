DROP TABLE IF EXISTS activities;
DROP TABLE IF EXISTS sights;
DROP TABLE IF EXISTS cities;
DROP TABLE IF EXISTS countries;

CREATE TABLE countries (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    city_id INT REFERENCES cities.id
);

CREATE TABLE cities (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    visited BOOLEAN,
    comment TEXT,
    sight_id INT REFERENCES sights.id
    activity_id INT REFERENCES activities.id
);

CREATE TABLE sights (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    visited BOOLEAN,
    comment TEXT,
    city_id INT REFERENCES cities.id
);

CREATE TABLE activities (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    completed BOOLEAN,
    comment TEXT,
    city_id INT REFERENCES cities.id
);
