

from flask import Blueprint, request
from flask_restful import Resource, Api


api_v1 = Blueprint("api", __name__)

api = Api(api_v1, prefix="/api/v1")



class RecipeResource(Resource):

    def get(self):
        return "Recipe"

    def post(self):
        print request.get_json()
        return "Application"

api.add_resource(RecipeResource, "/recipe")

