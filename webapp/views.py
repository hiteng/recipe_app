





from recipe_app.webapp.app import recipe_app
from flask import render_template

@recipe_app.route("/", methods=["GET"])
def home():

    return render_template("home.html")

