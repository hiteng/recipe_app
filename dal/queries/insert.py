

from recipe_app.dal import Session


class InsertOperations(object):
    def __init__(self):
        self.session = Session()

    def insert_obj(self, model_obj):
        print self.session
        self.session.add(model_obj)
        self.session.commit()






