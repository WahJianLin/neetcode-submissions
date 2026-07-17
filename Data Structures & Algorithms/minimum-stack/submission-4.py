class MinStack:
    stack = None
    least = None
    def __init__(self):
        self.stack = []
        self.least = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.least:
            self.least.append(val)
        else:
            if self.least[-1] >= val:
                self.least.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.least[-1]:
            self.least.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.least[-1]

