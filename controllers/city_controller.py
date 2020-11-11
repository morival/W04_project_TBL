from flask import Flask, render_template, request, redirect, Blueprint
from models.city import City
import repositories.city_repository as city_repository
import repositories.country_repository as country_repository

cities_blueprint = Blueprint("cities", __name__)


    # INDEX
@cities_blueprint.route("/cities")
def cities():
    cities = city_repository.select_all()
    return render_template("cities/index.html", cities=cities)


    # SHOW
@cities_blueprint.route("/cities/<id>")
def show_city(id):
    city = city_repository.select(id)
    return render_template("cities/show.html", city=city)


    # SHOW VISITED
@cities_blueprint.route("/cities/visited")
def visited_cities():
    visited_cities = []
    cities = city_repository.select_all()
    for city in cities:
        if city.visited == True:
            visited_cities.append(city)
    return render_template("cities/visited.html", visited_cities=visited_cities)


    # SHOW NOT VISITED
@cities_blueprint.route("/cities/not-visited")
def not_visited_cities():
    not_visited_cities = []
    cities = city_repository.select_all()
    for city in cities:
        if city.visited == False:
            not_visited_cities.append(city)
    return render_template("cities/not-visited.html", not_visited_cities=not_visited_cities)


    # NEW 
@cities_blueprint.route("/cities/<id>/new")
def new_city(id):
    sel_country = country_repository.select(id)
    countries = country_repository.select_all()
    return render_template("cities/new.html", sel_country=sel_country, countries=countries)


    # CREATE
@cities_blueprint.route("/cities", methods=['POST'])
def create_city():
    name = request.form['name']
    country_id = request.form['country_id']
    country = country_repository.select(country_id)
    visited = False
    comment = request.form['comment']
    new_city = City(name, country, visited, comment)
    city_repository.save(new_city)
    return redirect(f"/countries/{country_id}")


    # EDIT
@cities_blueprint.route("/cities/<id>/edit")
def edit_city(id):
    city = city_repository.select(id)
    return render_template("cities/edit.html", city=city)


    # UPDATE
@cities_blueprint.route("/cities/<id>", methods=['POST'])
def update_city(id):
    name = request.form['name']
    city = city_repository.select(id)
    city_id = city.id
    country_id = city.country.id
    country = country_repository.select(country_id)
    visited = city.visited
    comment = city.comment
    updated_city = City(name, country, visited, comment, id)
    city_repository.update(updated_city)
    return redirect(f"/cities/{city_id}")


    # VISIT 
@cities_blueprint.route("/cities/<id>/visit", methods=['POST'])
def visit(id):
    city = city_repository.select(id)
    city_id = city.id
    name = city.name
    country = city.country
    comment = city.comment
    visited = True
    visit_city = City(name, country, visited, comment, id)
    city_repository.update(visit_city)
    visit_city.country.visited = True
    country_repository.update(visit_city.country)
    return redirect(f"/cities/{city_id}")


    # COMMENT
@cities_blueprint.route("/cities/<id>/comment", methods=['POST'])
def comment(id):
    city = city_repository.select(id)
    city_id = city.id
    name = city.name
    country = city.country
    visited = city.visited
    comment = request.form['comment']
    commented_city = City(name, country, visited, comment, id)
    city_repository.update(commented_city)
    return redirect(f"/cities/{city_id}")


    # DELETE
@cities_blueprint.route("/cities/<id>/delete", methods=['POST'])
def delete_city(id):
    city = city_repository.select(id)
    country_id = city.country.id
    city_repository.delete(id)
    return redirect(f"/countries/{country_id}")
