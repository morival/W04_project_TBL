DROP TABLE IF EXISTS countries;
DROP TABLE IF EXISTS cities;
DROP TABLE IF EXISTS activities;
DROP TABLE IF EXISTS sights;


-- CREATE TABLE sights (
--     id SERIAL PRIMARY KEY,
--     name VARCHAR(255),
--     visited BOOLEAN,
--     comment TEXT,
-- );

-- CREATE TABLE activities (
--     id SERIAL PRIMARY KEY,
--     name VARCHAR(255),
--     completed BOOLEAN,
--     comment TEXT,
-- );

CREATE TABLE cities (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    visited BOOLEAN,
    comment TEXT,
    -- sight_id INT REFERENCES sights.id ON DELETE CASCADE,
    -- activity_id INT REFERENCES activities.id ON DELETE CASCADE
);

CREATE TABLE countries (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    city_id INT REFERENCES cities.id ON DELETE CASCADE
);