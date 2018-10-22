

from sqlalchemy.orm import synonym
import json
from ast import literal_eval
from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy_utils import ChoiceType
from recipe_app.dal import Base
from recipe_app.common.utils import get_utc_now


class Recipe(Base):
    TYPES = [
        (u"veg", "Veg"),
        (u"non-veg", "Non Veg")
    ]
    __tablename__ = "recipe"


    recipe_name = Column(String(100), primary_key=True)
    _ingredients = Column("ingredients", Text())
    instructions = Column(Text())
    serving_size = Column(Integer, default=1)
    category = Column(ChoiceType(TYPES))
    notes = Column(Text())
    created = Column(DateTime, nullable=False, default=get_utc_now())
    modified = Column(DateTime, nullable=False, default=get_utc_now(), onupdate=get_utc_now())

    @property
    def ingredients(self):
        return literal_eval(self._ingredients)


    @ingredients.setter
    def ingredients(self, value):
        self._ingredients = json.dumps(value)

    def as_dict(self):

        out_dict = {}
        for c in self.__table__.columns:
            if c.name in ['category']:
                out_dict[c.name] = getattr(self, c.name).value
            elif c.name in ['ingredients']:
                out_dict[c.name] = getattr(self, c.name)
            else:
                out_dict[c.name] = str(getattr(self, c.name))

        return out_dict

    ingredients = synonym("_ingredients", descriptor=ingredients)










