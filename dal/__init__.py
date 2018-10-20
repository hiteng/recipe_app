

from sqlalchemy.ext.declarative import declarative_base
from recipe_app.common.mysql_connector import engine
from sqlalchemy.orm import sessionmaker


Base = declarative_base()

Session = sessionmaker(bind=engine)


