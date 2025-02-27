class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        pos = nums.index(k)
        N = len(nums)
        bal = 0
        cnt = defaultdict(int)
        for i in range(pos, N):
            bal += 1 if nums[i] > k else(-1 if nums[i] < k else 0)
            cnt[bal] +=1
        bal = 0
        res = 0
        for i in range(pos, -1, -1):
            bal += 1 if nums[i] > k else(-1 if nums[i] < k else 0)
            # odd
            res +=cnt[-bal]
            # even
            res +=cnt[-bal + 1]
        return res

            