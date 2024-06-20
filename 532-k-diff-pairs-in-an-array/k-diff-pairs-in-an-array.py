class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0
        nums.sort()
        n = len(nums)
        def findExist(index, num):
            target = nums[index]
            l, r = 0, len(num) - 1
            while l <= r:
                mid = (l + r) // 2
                if abs(num[mid] - target) == k:
                    return True
                elif abs(num[mid] - target) < k:
                    l = mid + 1
                else:
                    r = mid - 1
            return False
        
        cnt = 0
        for i in range(n - 1):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if findExist(i, nums[i + 1:]):
                cnt += 1
        
        return cnt