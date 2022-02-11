import json

def encode_class_to_dict(self):
    """Take a class in argument and return a dict."""

    class_in_str = json.JSONEncoder(default=lambda o: o.__dict__).encode(self)
    class_in_dict = json.loads(class_in_str)

    return class_in_dict


def encode_json_to_dict(self):
    """Take a json document in argument and return a dict."""

    class_in_str = json.dumps(self)
    class_in_dict = json.loads(class_in_str)
    
    return class_in_dict
