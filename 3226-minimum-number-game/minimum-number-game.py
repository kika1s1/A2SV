class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        arr = []
        cnt = 0
        
        while len(nums) !=0:
            temp = min(nums)
            nums.remove(temp)
            sTemp = min(nums)
            nums.remove(sTemp)
            arr.append(sTemp)
            arr.append(temp)
        return arr

