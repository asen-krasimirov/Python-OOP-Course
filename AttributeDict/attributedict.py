

class AttributeDict(dict):

    def __init__(self, data: dict, **kwargs):
        super().__init__(kwargs)
        self.dict = data


test = AttributeDict({'test1': 1})