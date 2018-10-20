

from recipe_app.dal import Base
from recipe_app.dal.model.recipe import Recipe
from recipe_app.common.mysql_connector import engine


print Base.metadata.create_all(engine)