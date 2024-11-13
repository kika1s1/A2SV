class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        cnt = 0
        
        for index, num in enumerate(nums):
            left, right = index + 1, len(nums) - 1
            minim = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[index] + nums[mid] >= lower:
                    minim = mid
                    right = mid - 1
                else:
                    left = mid + 1
            left, right = index + 1, len(nums) - 1
            maxim = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[index] + nums[mid] <= upper:
                    maxim = mid
                    left = mid + 1
                else:
                    right = mid - 1
            
            if minim != -1 and maxim != -1 and minim <= maxim:
                cnt += (maxim - minim + 1)
        
        return cnt
