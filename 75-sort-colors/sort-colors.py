class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        freq=[0]*3
        for x in nums: 
            freq[x]+=1
        count=0
        for x in range(3):
            nums[count:count+freq[x]] = [x]*freq[x]
            count+= freq[x]

        