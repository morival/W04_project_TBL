from flask import Flask, render_template, request, redirect, Blueprint
from models.sight import Sight
import repositories.sight_repository as sight_repository
import repositories.city_repository as city_repository

sights_blueprint = Blueprint("sights", __name__)


    # INDEX
@sights_blueprint.route("/sights")
def sights():
    sights = sight_repository.select_all()
    return render_template("sights/index.html", sights=sights)


    # SHOW
@sights_blueprint.route("/sights/<id>")
def show_sight(id):
    sight = sight_repository.select(id)
    return render_template("sights/show.html", sight=sight)


    # SHOW VISITED
@sights_blueprint.route("/sights/visited")
def visited_sights():
    visited_sights = []
    sights = sight_repository.select_all()
    for sight in sights:
        if sight.visited == True:
            visited_sights.append(sight)
    return render_template("sights/visited.html", visited_sights=visited_sights)


    # SHOW NOT VISITED
@sights_blueprint.route("/sights/not-visited")
def not_visited_sights():
    not_visited_sights = []
    sights = sight_repository.select_all()
    for sight in sights:
        if sight.visited == False:
            not_visited_sights.append(sight)
    return render_template("sights/not-visited.html", not_visited_sights=not_visited_sights)


    # NEW 
@sights_blueprint.route("/sights/<id>/new")
def new_sight(id):
    city = city_repository.select(id)
    cities = city_repository.select_all()
    return render_template("sights/new.html", city=city, cities=cities)


    # CREATE
@sights_blueprint.route("/sight", methods=['POST'])
def create_sight():
    name = request.form['name']
    city_id = request.form['city_id']
    city = city_repository.select(city_id)
    visited = False
    comment = request.form['comment']
    new_sight = Sight(name, city, visited, comment)
    sight_repository.save(new_sight)
    return redirect(f"/sights/{city_id}")


    # EDIT
@sights_blueprint.route("/sights/<id>/edit")
def edit_sight(id):
    sight = sight_repository.select(id)
    return render_template("sights/edit.html", sight=sight)


    # UPDATE
@sights_blueprint.route("/sights/<id>", methods=['POST'])
def update_sight(id):
    name = request.form['name']
    sight = sight_repository.select(id)
    sight_id = sight.id
    city_id = sight.city.id
    city = city_repository.select(city_id)
    visited = sight.visited
    comment = request.form['comment']
    updated_sight = Sight(name, city, visited, comment, id)
    sight_repository.update(updated_sight)
    return redirect(f"/sights/{sight_id}")


    # VISIT 
@sights_blueprint.route("/sights/<id>/visit", methods=['POST'])
def visit(id):
    sight = sight_repository.select(id)
    sight_id = sight.id
    name = sight.name
    city = sight.city
    comment = sight.comment
    visited = True
    visit_sight = Sight(name, city, visited, comment, id)
    sight_repository.update(visit_sight)
    visit_sight.city.visited = True
    city_repository.update(visit_sight.city)
    return redirect(f"/sights/{sight_id}")


    # DELETE
@sights_blueprint.route("/sights/<id>/delete", methods=['POST'])
def delete_sight(id):
    sight = sight_repository.select(id)
    city_id = sight.city.id
    sight_repository.delete(id)
    return redirect(f"/cities/{city_id}")
