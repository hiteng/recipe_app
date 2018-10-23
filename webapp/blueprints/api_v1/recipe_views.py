

from flask import Blueprint, request, jsonify
from flask_restful import Resource, Api
from recipe_app.webapp.blueprints.api_v1.controller import create_recipe, get_all_recipes, delete_recipe, update_recipe

api_v1 = Blueprint("api", __name__)

api = Api(api_v1, prefix="/api/v1")





class RecipeResource(Resource):


    def get(self):
        output = get_all_recipes()
        return jsonify(output)


    def post(self, recipe_name=None):
        attr_dict = request.get_json()

        status, msg = create_recipe(attr_dict)

        return {"Status": status, "msg": msg}

    def put(self, recipe_name=None):
        attr_dict = request.get_json()
        
        status, msg = update_recipe(recipe_name, attr_dict)

        return {"Status": status, "msg": msg}


    def delete(self, recipe_name=None):
        status, msg = delete_recipe(recipe_name)
        return {"Status": status, "msg": msg}

#api.add_resource(RecipeResource, "/recipe")
api.add_resource(RecipeResource, "/recipe/<recipe_name>")

