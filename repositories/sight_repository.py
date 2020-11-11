from db.run_sql import run_sql

from models.sight import Sight

import repositories.city_repository as city_repository


def save(sight):
    sql = "INSERT INTO sights (name, city_id, visited, comment) VALUES ( %s, %s, %s, %s ) RETURNING id"
    values = [sight.name, sight.country.id, sight.visited, sight.comment]
    results = run_sql( sql, values )
    sight.id = results[0]['id']
    return sight


def select_all():
    sights = []

    sql = "SELECT * FROM sights"
    results = run_sql(sql)

    for row in results:
        city = city_repository.select(row['city_id'])
        sight = Sight(row['name'], city, row['visited'], row['comment'], row['id'])
        sights.append(sight)
    return sights


def select(id):
    sight = None
    sql = "SELECT * FROM sights WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        city = city_repository.select(result['city_id'])
        sight = Sight(result['name'], city, result['visited'], result['comment'], result['id'])
    return sight


def delete_all():
    sql = "DELETE FROM sights"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM sights WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(sight):
    sql = "UPDATE sights SET (name, city_id, visited, comment) = (%s, %s, %s, %s) WHERE id = %s"
    values = [sight.name, sight.country.id, sight.visited, sight.comment, sight.id]
    run_sql(sql, values)


def sights(id):
    sights = []

    sql = "SELECT * FROM sights WHERE city_id = %s ORDER by name ASC"
    values = [id]
    results = run_sql(sql, values)

    for row in results:
        city = city_repository.select(row['city_id'])
        sight = Sight(row['name'], city, row['visited'], row['comment'], row['id'])
        sights.append(sight)
    return sights
