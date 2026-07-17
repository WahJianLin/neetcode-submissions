class MinStack:
    stack=None

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        low = self.stack[-1]
        for v in self.stack:
            low = min(low,v)
        return low

