class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums[::k]
        n = len(nums)
        ans = []
        for i in range(n - k + 1):
            sub = (nums[i:i+k])
            is_true = all(nums[j] - nums[j-1] == 1 for j in range(i+1, i+k))
            # print(list(is_true))
            if is_true:
                ans.append(sub[-1])
            else:
                ans.append(-1)
            
        return ans