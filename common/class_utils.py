


def create_object(class_name, attr_dict):
    obj = class_name()

    for attr, val in attr_dict.iteritems():

        if hasattr(obj, attr):
            setattr(obj, attr, val) # obj.attr = val

    return obj
