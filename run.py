

from recipe_app.webapp.app import recipe_app


recipe_app.run(debug=True, host='0.0.0.0', threaded=True, port=8000)