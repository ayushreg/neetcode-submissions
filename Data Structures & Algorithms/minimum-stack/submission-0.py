class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        return None

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        minValue = float('inf')
        for num in self.stack:
            minValue = min(num, minValue)
        return minValue
