class RecentCounter:

    def __init__(self):
        self.calls = []
        self.start = 0
        

    def ping(self, t: int) -> int:
        if not self.calls:
            self.calls.append(t)
            return 1
        else:
            while self.start < len(self.calls) and   t - self.calls[self.start] > 3000:
                self.start +=1
            if self.start >= len(self.calls):
                self.calls.append(t)
                return 1
            else:
                self.calls.append(t)
                return len(self.calls) - self.start
            

        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)