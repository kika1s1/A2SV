class Solution:
    def findLucky(self, arr: List[int]) -> int:
        arr.sort()
        ans = -1
        for i in arr:
            if i == arr.count(i):
                ans = i

        return ans