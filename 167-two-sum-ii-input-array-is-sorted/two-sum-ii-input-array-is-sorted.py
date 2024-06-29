class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1
        while l <=r:
            total = numbers[l] + numbers[r]
            if total == target:
                return [l+1, r + 1]
            elif target > total:
                # r -=1
                l +=1
            else:
                r -=1
            