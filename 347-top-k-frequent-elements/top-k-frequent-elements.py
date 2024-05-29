class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = sorted(Counter(nums).items(), key=lambda x:-x[1])
        ans = []
        for i in range(k):
            ans.append(cnt[i][0])
        

        return ans