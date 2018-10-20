

from recipe_app.dal.model.recipe import Recipe
from recipe_app.common.class_utils import create_object
from recipe_app.dal.queries.insert import InsertOperations


def create_recipe(attr_dict):
    recipe_obj = create_object(Recipe, attr_dict)
    recipe_obj.ingredients = attr_dict.get("ingredients")
    print recipe_obj.__dict__
    ins_obj = InsertOperations()
    ins_obj.insert_obj(recipe_obj)

if __name__ == '__main__':

    a = {"recipe_name": "Cake", "ingredients": ["Bun", "Pattie"], "instructions": "Heat it !",
         "category": "vegan", "notes": "trying to do "}

    create_recipe(a)





    #
    # recipe_name = Column(String(100), primary_key=True)
    # ingredients = Column(Text())
    # _instructions = Column(Text())
    # serving_size = Column(Integer, default=1)
    # category = Column(ChoiceType(TYPES))
    # notes = Column(Text())
    # created = Column(DateTime, nullable=False, server_default=get_utc_now())
    # modified = Column(DateTime, nullable=False, server_default=get_utc_now(), onupdate=get_utc_now())