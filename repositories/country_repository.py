from db.run_sql import run_sql

from models.country import Country
from models.continent import Continent

import repositories.continent_repository as continent_repository

def save(country):
    sql = "INSERT INTO countries (name, continent_id) VALUES (%s, %s) RETURNING id"
    values = [country.name, country.continent.id]
    results = run_sql(sql, values)
    country.id = results[0]['id']
    return country


def select_all():
    countries = []

    sql = "SELECT * FROM countries"
    results = run_sql(sql)

    for row in results:
        continent = continent_repository.select(row['continent_id'])
        country = Country(row['name'], continent, row['id'])
        countries.append(country)
    return countries


def select(id):
    country = None
    sql = "SELECT * FROM countries WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        continent = continent_repository.select(result['continent_id'])
        country = Country(result['name'], continent, result['id'])
    return country


### Add City to Cities

# def cities(country):
#     cities = []

#     sql = "SELECT cities.* FROM cities INNER JOIN ..."


def delete_all():
    sql = "DELETE FROM countries"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM countries WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(country):
    sql = "UPDATE countries SET (name, continent_id) = (%s, %s) WHERE id = %s"
    values = [country.name, country.continent.id, country.id]
    run_sql(sql, values)