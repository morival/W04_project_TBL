from db.run_sql import run_sql

from models.country import Country
from models.city import City

import repositories.city_repository as city_repository

def save(country):
    sql = "INSERT INTO countries(name, continent, city_id) VALUES (%s, %s, %s) RETURNING id"
    values = [country.name, country.continent, country.city.id]
    results = run_sql(sql, values)
    country.id = results[0]['id']
    return country


def select_all():
    countries = []

    sql = "SELECT * FROM countries"
    results = run_sql(sql)

    for row in results:
        city = city_repository.select(row['city_id'])
        country = Country(row['name'], row['continent'], city, row['id'])
        countries.append(country)
    return countries


def select(id):
    country = None
    sql = "SELECT * FROM countries WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        city = city_repository.select(result['city_id'])
        country = Country(result['name'], result['continent'], city, result['id'])
        return country


### select city from existing cities

# def city(country):
#     sql = "SELECT * FROM cities WHERE id = %s"
#     values = [country.city.id]
#     results = run_sql(sql, values)[0]
#     city = City(results['name'], results['visited'], results['comment'], results['sight'], results['activity'], results['id'])
#     return city


def delete_all():
    sql = "DELETE FROM countries"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM countries WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(country):
    sql = "UPDATE countries SET (name, continent, city_id) = (%s, %s, %s) WHERE id = %s"
    values = [country.name, country.continent, country.city.id, country.id]
    run_sql(sql, values)