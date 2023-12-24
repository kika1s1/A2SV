class Solution:
    def arrayChange(self, nums, ops):
        mp = {}
        
        for i in range(len(nums)):
            mp[nums[i]] = i
        
        for op in ops:
            currele, newele = op[0], op[1]
            nums[mp[currele]] = newele
            mp[newele] = mp[currele]
        
        return nums