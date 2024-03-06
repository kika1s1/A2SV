class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = []
        for i, num in enumerate(nums):
            if num == target:
                ans.append(i)
                break
        for i,num in enumerate(nums[::-1]):
            if num == target:
                ans.append(len(nums)-1-i)
                break
        return ans if len(ans) !=0 else [-1, -1]