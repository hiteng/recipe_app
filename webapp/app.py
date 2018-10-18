

import os
from flask import Flask

template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static", "templates")
recipe_app = Flask(__name__, static_url_path='/static', static_folder='static', template_folder='static/templates')


from recipe_app.webapp.blueprints.api_v1.recipe_views import api_v1

recipe_app.register_blueprint(api_v1)

