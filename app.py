from flask import Flask, render_template

# from controllers.activity_controller import activities_blueprint
# from controllers.city_controller import cities_blueprint
# from controllers.country_controller import countries_blueprint
# from controllers.sight_controller import sights_blueprint

app = Flask(__name__)

# app.register_blueprint(activities_blueprint)
# app.register_blueprint(cities_blueprint)
# app.register_blueprint(countries_blueprint)
# app.register_blueprint(sights_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
