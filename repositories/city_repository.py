from db.run_sql import run_sql

from models.city import City



def save(city):
    sql = "INSERT INTO cities (name, visited, comment, sight, activity) VALUES ( %s, %s, %s, %s, %s ) RETURNING id"
    values = [city.name, city.visited, city.comment, city.sight, city.activity]
    results = run_sql( sql, values )
    city.id = results[0]['id']
    return city


def select_all():
    cities = []

    sql = "SELECT * FROM cities"
    results = run_sql(sql)

    for row in results:
        city = City(row['name'], row['visited'], row['comment'], row['sight'], row['activity'], row['id'])
        cities.append(city)
    return cities


def select(id):
    city = None
    sql = "SELECT * FROM cities WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        city = City(result['name'], result['visited'], result['comment'], result['sight'], result['activity'], result['id'])
    return city


def delete_all():
    sql = "DELETE FROM cities"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM cities WHERE id = %s"
    values = [id]
    run_sql(sql, values)