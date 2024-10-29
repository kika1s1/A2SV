class MyHashMap:
    def __init__(self):
        self.map = [[] for _ in range(1000)]

    def put(self, key: int, value: int) -> None:
        index = key % 1000
        for i, (k, v) in enumerate(self.map[index]):
            if k == key:
                self.map[index][i] = (key, value)
                return
        self.map[index].append((key, value))

    def get(self, key: int) -> int:
        index = key % 1000
        for k, v in self.map[index]:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        index = key % 1000
        for i, (k, v) in enumerate(self.map[index]):
            if k == key:
                del self.map[index][i]
                return



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)