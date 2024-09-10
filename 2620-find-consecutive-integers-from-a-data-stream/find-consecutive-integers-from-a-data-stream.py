class DataStream:

    def __init__(self, value: int, k: int):
        self.nums = []
        self.length = k
        self.num = value
        self.cnt = 0
        self.stack = []
        

    def consec(self, num: int) -> bool:
        if num == self.num:
            self.cnt +=1
            if self.cnt >=self.length:
                return True
            return False
        else:
            self.cnt = 0
            if self.cnt >=self.length:
                return True
            return False

        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)