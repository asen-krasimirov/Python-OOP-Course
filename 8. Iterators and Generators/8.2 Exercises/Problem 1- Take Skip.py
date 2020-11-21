

class take_skip:
    step: int
    count: int

    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.cur_step = step * -1
        self.cur_count = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.cur_step += self.step
        self.cur_count += 1

        if self.cur_count > self.count:
            raise StopIteration

        return self.cur_step


numbers = take_skip(-1, 10)
for number in numbers:
    print(number)
