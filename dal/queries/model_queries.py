

from recipe_app.dal import Session


class ModelQueries(object):
    def __init__(self):
        self.session = Session()

    def insert_obj(self, model_obj):
        print self.session
        self.session.add(model_obj)
        self.session.commit()

    def update_obj(self, model_class, pri_key, attr_dict):

        model_obj = self.session.query(model_class).get(pri_key)
        self.update_obj_attr(model_obj, attr_dict)
        self.session.commit()

    def update_obj_attr(self,model_object, kwargs):
        for key, value in kwargs.items():
            setattr(model_object, key, value)

    def delete_obj(self, model_class, pri_key):
        model_obj = self.session.query(model_class).get(pri_key)
        self.session.delete(model_obj)
        self.session.commit()

    def get_obj(self, model_class, pri_key):
        return self.session.query(model_class).get(pri_key)

    def get_all_obj(self, model_class):
        return self.session.query(model_class).all()

    def close_session(self):

        return self.session.close()







