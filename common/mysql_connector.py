



from sqlalchemy.engine import create_engine
engine = create_engine("mysql+pymysql://hiteng:admin123@localhost/recipe_db?host=localhost?port=3306")
conn = engine.connect()
print conn
