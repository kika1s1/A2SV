class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        pos = nums.index(k)
        cnt = defaultdict(int)
        bal = 0
        for i in range(pos, len(nums)):
            bal += int(nums[i] > k) - int(nums[i] < k)
            cnt[bal] +=1
        res = 0
        bal = 0
        for i in reversed(range(pos+1)):
            bal +=int(nums[i] > k) - int(nums[i] < k)
            res +=cnt[-bal] # odd
            res +=cnt[-bal + 1] # Even
        return res