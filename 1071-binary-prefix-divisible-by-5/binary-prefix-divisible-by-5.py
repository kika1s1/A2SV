class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        ans = []
        pref = ""
        for i in nums:
            pref +=str(i)
            num = int(pref, 2)
            if num%5 == 0:
                ans.append(True)
            else:
                ans.append(False)
        return ans