class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        N = len(nums)
        
        for i in range(N):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left, right = i + 1, N - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total == 0:
                    ans.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        
        return ans
