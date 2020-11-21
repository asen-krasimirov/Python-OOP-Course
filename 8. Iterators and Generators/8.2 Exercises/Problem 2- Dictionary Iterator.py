

class dictionary_iter:
    data: list

    def __init__(self, data: dict):
        self.data = [(key, val) for key, val in data.items()]
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index >= len(self.data):
            raise StopIteration

        return self.data[self.index]


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
