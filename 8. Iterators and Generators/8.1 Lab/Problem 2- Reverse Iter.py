

class reverse_iter:

    def __init__(self, iterable):
        self.iterable = iterable
        self.index = len(self.iterable) - 1

    def __iter__(self):
        return self

    def __next__(self):
        cur_idx, self.index = self.index, self.index - 1
        if cur_idx < 0:
            raise StopIteration
        return self.iterable[cur_idx]


# Solution with generator
def reverse_iter(iterable):
    index = len(iterable)
    while True:
        index -= 1
        if index < 0:
            break
        yield iterable[index]


for item in reverse_iter([1, 2, 3, 4]):
    print(item)
