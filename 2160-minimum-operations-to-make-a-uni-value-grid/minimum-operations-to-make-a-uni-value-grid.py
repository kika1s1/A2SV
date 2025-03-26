class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        values = [num for row in grid for num in row]
        
        remainder = values[0] % x
        for num in values:
            if num % x != remainder:
                return -1 
        def quickSelect(nums, k):
            pivot = random.choice(nums)
            left = [num for num in nums if num < pivot]
            mid = [num for num in nums if num == pivot]
            right = [num for num in nums if num > pivot]
            
            if k < len(left):
                return quickSelect(left, k)
            elif k < len(left) + len(mid):
                return mid[0] 
            else:
                return quickSelect(right, k - len(left) - len(mid))

        median = quickSelect(values, len(values) // 2)
        
        return sum(abs(num - median) // x for num in values)
