

from flask import Blueprint, request, jsonify
from flask_restful import Resource, Api
from recipe_app.webapp.blueprints.api_v1.controller import create_recipe, get_all_recipes

api_v1 = Blueprint("api", __name__)

api = Api(api_v1, prefix="/api/v1")





class RecipeResource(Resource):


    def get(self):
        output = get_all_recipes()
        return jsonify(output)


    def post(self):
        attr_dict = request.get_json()

        status, msg = create_recipe(attr_dict)

        return {"Status": status, "msg": msg}

api.add_resource(RecipeResource, "/recipe")

