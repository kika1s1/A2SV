class MinStack:

    def __init__(self):
        self.items = []

    def push(self, val: int) -> None:
        self.items.append(val)
        

    def pop(self) -> None:
        return self.items.pop()

    def top(self) -> int:
        return self.items[-1]
        

    def getMin(self) -> int:
        return min(self.items)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()