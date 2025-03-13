class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        
        def is_zero_array(k: int) -> bool:
            diff = [0] * (n + 1)  
            temp_nums = nums[:]  
            for i in range(k):
                l, r, val = queries[i]
                diff[l] -= val
                if r + 1 < n:
                    diff[r + 1] += val

            current = 0
            for i in range(n):
                current += diff[i]
                temp_nums[i] += current  
            return all(x <= 0 for x in temp_nums)

        left, right = 0, len(queries)
        answer = -1
        while left <= right:
            mid = (left + right) // 2
            if is_zero_array(mid):
                answer = mid
                right = mid - 1 
            else:
                left = mid + 1  

        return answer
