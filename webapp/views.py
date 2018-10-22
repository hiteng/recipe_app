





from recipe_app.webapp.app import recipe_app
from flask import render_template
from recipe_app.webapp.blueprints.api_v1.controller import get_all_recipes

@recipe_app.route("/", methods=["GET"])
def home():
    all_recipes = get_all_recipes()
    return render_template("home.html", all_recipes=all_recipes)

