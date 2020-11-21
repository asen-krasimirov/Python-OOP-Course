

class sequence_repeat:
    count: int

    def __init__(self, sequence, count: int):
        self.sequence = sequence
        self.count = count
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count <= self.index+1:
            raise StopIteration
        self.index += 1
        return self.sequence[self.index % len(self.sequence)]


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end='')
