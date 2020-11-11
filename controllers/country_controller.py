from flask import Flask, render_template, request, redirect, Blueprint
from models.country import Country
import repositories.country_repository as country_repository
import repositories.continent_repository as continent_repository
import repositories.city_repository as city_repository

countries_blueprint = Blueprint("countries", __name__)


    # INDEX
@countries_blueprint.route("/countries")
def countries():
    countries = country_repository.select_all()
    cities = city_repository.select_all()
    return render_template("countries/index.html", countries=countries, cities=cities)


    # SHOW
@countries_blueprint.route("/countries/<id>")
def show_country(id):
    cities = city_repository.cities(id)
    country = country_repository.select(id)
    return render_template("countries/show.html", country=country, cities=cities)


    # NEW
@countries_blueprint.route("/countries/new", methods=['GET'])
def new_country():
    continents = continent_repository.select_all()
    return render_template("countries/new.html", continents=continents)


    # CREATE
@countries_blueprint.route("/countries", methods=['POST'])
def create_country():
    continent_id = request.form['continent_id']
    name = request.form["name"]
    continent = continent_repository.select(continent_id)
    visited = False
    new_country = Country(name, continent, visited)
    country_repository.save(new_country)
    country_id = new_country.id
    return redirect(f"/countries/{country_id}")


    # EDIT
@countries_blueprint.route("/countries/<id>/edit")
def edit_country(id):
    continents = continent_repository.select_all()
    country = country_repository.select(id)
    sel_continent = country.continent.id
    return render_template("countries/edit.html", country=country, sel_continent=sel_continent, continents=continents)


    # UPDATE
@countries_blueprint.route("/countries/<id>", methods=['POST'])
def update_country(id):
    name = request.form['name']
    continent_id = request.form['continent_id']
    continent = continent_repository.select(continent_id)
    country = country_repository.select(id)
    visited = country.visited
    updated_country = Country(name, continent, visited, id)
    country_repository.update(updated_country)
    country_id = country.id
    return redirect(f"/countries/{country_id}")


    # SEARCH
@countries_blueprint.route("/search", methods=['GET'])
def search():
    continents = continent_repository.select_all()
    countries = country_repository.select_all()
    cities = city_repository.select_all()
    return render_template("search.html",continents=continents, countries=countries, cities=cities)


    # SEARCH RESULTS
@countries_blueprint.route("/search", methods=['POST'])
def search_results():
    search_country = []
    search_city = []
    search_key = request.form['search']
    key = search_key.lower()
    countries = country_repository.select_all()
    cities = city_repository.select_all()
    for country in countries:
        if country.name.lower() == key:
            search_country.append(country)
    for city in cities:
        if city.name.lower() == key:
            search_city.append(city)
        elif city.country.name.lower() == key:
            search_city.append(city)
    return render_template("/search.html",countries=countries, cities=cities, search_city=search_city, search_country=search_country)


    # DELETE '/countries/<id>'
@countries_blueprint.route("/countries/<id>/delete", methods=['POST'])
def delete_country(id):
    country_repository.delete(id)
    return redirect("/countries")