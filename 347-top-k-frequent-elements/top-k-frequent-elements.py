class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        n = Counter(nums)
        b = sorted(n.items(), key=lambda item: item[1], reverse=True)
        ans = []
        for i in range(k):
            ans.append(b[i][0])
            
        return ans