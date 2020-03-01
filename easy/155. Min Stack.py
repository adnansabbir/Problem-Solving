

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_number = None

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.min_number:
            self.min_number = x
        else:
            self.min_number = min(self.min_number, x)

    def pop(self) -> None:
        popped = self.stack.pop()
        if popped == self.min_number:
            self.min_number = min(self.stack) if self.stack else None
        return popped

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_number


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(5)
obj.push(3)
obj.push(10)
obj.push(2)

print(obj.top())
print(obj.getMin())
obj.pop()
print(obj.getMin())
