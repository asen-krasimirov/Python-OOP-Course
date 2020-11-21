

def solution():

    def integers(cur_integer=0):
        while True:
            cur_integer += 1
            yield cur_integer

    def halves():
        for i in integers():
            yield i / 2

    def take(n, seq):
        count = 0
        array = []
        for num in seq:
            if count >= n:
                return array
            array.append(num)
            count += 1

    return take, halves, integers


take = solution()[0]
halves = solution()[1]
print(take(5, halves()))
