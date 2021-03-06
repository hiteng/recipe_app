
from sqlalchemy import exc
from recipe_app.dal.model.recipe import Recipe
from recipe_app.common.class_utils import create_object
from recipe_app.dal.queries.model_queries import ModelQueries


def create_recipe(attr_dict):
    try:

        recipe_obj = create_object(Recipe, attr_dict)
        recipe_obj.ingredients = attr_dict.get("ingredients")
        qr_obj = ModelQueries()
        qr_obj.insert_obj(recipe_obj)
        qr_obj.close_session()
    except exc.IntegrityError as e:
        # Todo logging
        print e
        return False, "Recipe already exists by name: {}".format(attr_dict.get("recipe_name"))
    except Exception as e:
        # Todo logging
        print e
        return False, "Failed to create recipe by name: {}".format(attr_dict.get("recipe_name"))
    return True, "New recipe created by name: {}".format(attr_dict.get("recipe_name"))


def update_recipe(recipe_name, attr_dict):
    try:
        qr_obj = ModelQueries()
        qr_obj.update_obj(Recipe, recipe_name, attr_dict)
        qr_obj.close_session()
    except Exception as e:
        return False, "Failed to update recipe by name: {}".format(recipe_name)
    return True, "Updated recipe by name: {}".format(recipe_name)


def delete_recipe(recipe_name):
    try:
        qr_obj = ModelQueries()
        qr_obj.delete_obj(Recipe, recipe_name)
    except Exception as e:
        return False, "Failed to delete recipe by name: {}".format(recipe_name)
    return True, "Deleted recipe by name: {}".format(recipe_name)

def get_all_recipes(recipe_name=None):
    qr_obj = ModelQueries()
    output_list = []
    if recipe_name:
        obj = qr_obj.get_obj(Recipe, recipe_name)
        return obj.as_dict()
    objs = qr_obj.get_all_obj(Recipe)
    return [obj.as_dict() for obj in objs]


if __name__ == '__main__':

    a = {"recipe_name": "Cake", "ingredients": ["Bun", "Pattie"], "instructions": "Heat it !", "Serving Size": 2,
         "category": "veg", "notes": "trying to do "}

    b = {"ingredients": ["Bun", "Pattie", "Cheese"], "instructions": "Warm",
         "category": "veg", "notes": "trying to do "}

    #create_recipe(a)
    update_recipe("aaaa", b)
    #delete_recipe("Pasta")
    #print get_all_recipes()




    #
    # recipe_name = Column(String(100), primary_key=True)
    # ingredients = Column(Text())
    # _instructions = Column(Text())
    # serving_size = Column(Integer, default=1)
    # category = Column(ChoiceType(TYPES))
    # notes = Column(Text())
    # created = Column(DateTime, nullable=False, server_default=get_utc_now())
    # modified = Column(DateTime, nullable=False, server_default=get_utc_now(), onupdate=get_utc_now())