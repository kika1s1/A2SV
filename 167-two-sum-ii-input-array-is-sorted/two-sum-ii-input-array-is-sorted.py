class Solution(object):
    def twoSum(self, n, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        first = 0
        last = len(n)-1
        while first < last:
            if n[first] + n[last] == target:
                return [first+1, last+1]
            elif n[first] + n[last] < target:
                first += 1
            elif n[first] + n[last] > target:
                last -= 1

            
        