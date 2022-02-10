from json import JSONEncoder


class MyEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

    def encode_class(_class):
        return MyEncoder().encode(_class)


def encode_class(self):
    print(MyEncoder.encode_class(self))