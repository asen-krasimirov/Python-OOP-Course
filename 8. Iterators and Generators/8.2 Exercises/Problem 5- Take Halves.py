

def solution():

    def integers(cur_integer=1):
        while True:
            yield cur_integer
            cur_integer += 1

    def halves():
        for i in integers():
            yield i / 2

    def take(n, seq):
        return [next(seq) for _ in range(n)]

        # return list(n for n, _ in zip(seq, range(n)))  # Alternative solution

        # Third solution
        # count = 0
        # array = []
        # for num in seq:
        #     if count >= n:
        #         return array
        #     array.append(num)
        #     count += 1

    return take, halves, integers


# take = solution()[0]
# halves = solution()[1]
# print(take(5, halves()))
