

class Stack:
    data: list

    def __init__(self):
        self.data = []

    def push(self, item: str):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self) -> str:
        return self.data[-1]

    def is_empty(self) -> bool:
        return False if self.data else True

    def __str__(self):
        return f"[{', '.join(reversed(self.data))}]"


stack = Stack()
stack.push("apple")
stack.push("carrot")
print(str(stack))  # -> '[carrot, apple]'
stack.pop()  # -> 'carrot'
stack.peek()  # -> 'apple'
stack.push("cucumber")
print(str(stack))  # -> '[cucumber, apple]')
print(stack.is_empty())