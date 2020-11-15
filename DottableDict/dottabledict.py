

class DottableDict(dict):

    def __init__(self, data: dict, *args):
        super().__init__(args)
        self.dictionary = data

    def __getitem__(self, item):
        items = item.split('.')
        if len(items) == 1:
            return self.dictionary[item]

        result = self.dictionary
        while True:
            if len(items)-1 < 0:
                break
            result = result[items.pop(0)]
        return result


dotted_dict = DottableDict({'test1': {'test2': {'test3': 'passed'}}})

print(dotted_dict['test1'])
print(dotted_dict['test1.test2'])
print(dotted_dict['test1.test2.test3'])
