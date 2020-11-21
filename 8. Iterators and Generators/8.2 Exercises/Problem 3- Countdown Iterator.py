

class countdown_iterator:
    count: int

    def __init__(self, count: int):
        self.count = count

    def __iter__(self):
        return self

    def __next__(self):
        cur_count, self.count = self.count, self.count-1
        if cur_count < 0:
            raise StopIteration

        return cur_count


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")
