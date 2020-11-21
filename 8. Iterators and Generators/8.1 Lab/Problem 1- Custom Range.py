

class custom_range:
    start: int
    end: int
    
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end
    
    def __iter__(self):
        return self
    
    def __next__(self):
        cur_var, self.start = self.start, self.start + 1
        if cur_var > self.end:
            raise StopIteration
        return cur_var


one_to_ten = custom_range(1, 10)
for num in one_to_ten:
    print(num)
