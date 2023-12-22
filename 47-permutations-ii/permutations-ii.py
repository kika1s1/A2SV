class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        allList = list(permutations(nums))
        ans = []
        for i in allList:
            if list(i) not in ans:
                ans.append(list(i))
        return ans
                