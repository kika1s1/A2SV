class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.cnt = 0
        

    def consec(self, num: int) -> bool:
        if self.value != num:
            self.cnt = 0
        else:
            self.cnt +=1
        return self.cnt >=self.k

        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)