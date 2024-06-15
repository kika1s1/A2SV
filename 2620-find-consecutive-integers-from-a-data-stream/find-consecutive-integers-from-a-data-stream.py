class DataStream:

    def __init__(self, value: int, k: int):
        self.k = k
        self.items = []
        self.value = value
        self.cnt = 0
    def consec(self, num: int) -> bool: 
        if self.value == num:
            self.cnt +=1
        else:
            self.cnt = 0
        if self.cnt >=self.k:
            return True
        return False

        # self.items.append(num)
        # if len(self.items) < self.k:
        #     return False
        # return len(set(self.items[-self.k:])) == 1 and self.items[-1] == num
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)