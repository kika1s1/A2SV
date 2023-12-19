class CustomStack:

    def __init__(self, maxSize: int):
        self.items = []
        self.maxSize = maxSize

        

    def push(self, x: int) -> None:
        if len(self.items) == self.maxSize:
            return
        self.items.append(x)

        

    def pop(self) -> int:
        if len(self.items) == 0:
            return -1
        return self.items.pop()

        

    def increment(self, k: int, val: int) -> None:
        if k > len(self.items):
            for i in range(len(self.items)):
                temp = self.items[i]
                self.items[i] = temp + val
        else:
            for i in range(k):
                temp = self.items[i]
                self.items[i] = temp + val




# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)