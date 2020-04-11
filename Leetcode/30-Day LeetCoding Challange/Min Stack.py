class MinStack:

    def __init__(self):
        self._stack = []

    def push(self, x: int) -> None:
        if not self._stack:
            self._stack.append((x, x))
        else:
            if x < self._stack[-1][1]:
                self._stack.append((x, x))
            else:
                self._stack.append((x, self._stack[-1][1]))

    def pop(self) -> None:
        return self._stack.pop()[0]

    def top(self) -> int:
        return self._stack[-1][0]

    def getMin(self) -> int:
        return self._stack[-1][1]


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

for i in range(0, 10, 1):
    obj.push(i)

# print(obj._stack)
