class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 !=0:
            return False
        poss_sum = set([0])
        midd = total//2
        for num in nums:
            new_set = set()
            for j in poss_sum:
                new_set.add(num + j)
            poss_sum.update(new_set)
        if midd in poss_sum:
            return True
        else:
            return False
