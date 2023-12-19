class Solution:
    def findLucky(self, arr: List[int]) -> int:
        arr.sort()
        ans = -1
        repHash = Counter(arr)
        for i, j in repHash.items():
            if i == j:
                ans = i
        return ans