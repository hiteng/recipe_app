





from recipe_app.webapp.app import recipe_app
from flask import render_template, request
from recipe_app.webapp.blueprints.api_v1.controller import get_all_recipes

@recipe_app.route("/", methods=["GET"])
def home():
    all_recipes = get_all_recipes()
    return render_template("home.html", all_recipes=all_recipes)


@recipe_app.route("/add", methods=["GET", "POST"])
def add():

    return render_template("add.html")


@recipe_app.route("/edit", methods=["GET", "POST"])
def edit():

    recipe_name = request.args.get('recipe_name')
    recipe_name = recipe_name.strip()
    print recipe_name
    recipe = get_all_recipes(recipe_name)
    return render_template("edit.html", recipe=recipe)

