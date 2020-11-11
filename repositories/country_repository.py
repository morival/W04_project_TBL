from db.run_sql import run_sql

from models.country import Country

import repositories.continent_repository as continent_repository

def save(country):
    sql = "INSERT INTO countries (name, continent_id, visited) VALUES (%s, %s, %s) RETURNING id"
    values = [country.name, country.continent.id, country.visited]
    results = run_sql(sql, values)
    country.id = results[0]['id']
    return country


def select_all():
    countries = []

    sql = "SELECT * FROM countries"
    results = run_sql(sql)

    for row in results:
        continent = continent_repository.select(row['continent_id'])
        country = Country(row['name'], continent, row['visited'], row['id'])
        countries.append(country)
    return countries


def select(id):
    country = None
    sql = "SELECT * FROM countries WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        continent = continent_repository.select(result['continent_id'])
        country = Country(result['name'], continent, result['visited'], result['id'])
    return country


def delete_all():
    sql = "DELETE FROM countries"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM countries WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(country):
    sql = "UPDATE countries SET (name, continent_id, visited) = (%s, %s, %s) WHERE id = %s"
    values = [country.name, country.continent.id, country.visited, country.id]
    run_sql(sql, values)


