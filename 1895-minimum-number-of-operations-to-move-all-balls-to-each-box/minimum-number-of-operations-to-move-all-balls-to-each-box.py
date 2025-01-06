class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = []
        for index, num in enumerate(boxes):
            position = index
            add = 0
            for i, num in enumerate(boxes):
                if num == "1":
                    add +=abs(position-i)
            ans.append(add)
        return ans
                