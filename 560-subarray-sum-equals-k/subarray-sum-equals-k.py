class Solution(object):
    def subarraySum(self, nums, k):
        
        currSum = 0
        ansCount = 0
        prevSums = {0:1}        
        
        for num in nums:
            
            currSum += num
            
            if currSum - k in prevSums:
                ansCount += prevSums[currSum - k]
                
            if currSum in prevSums:
                prevSums[currSum] += 1
            else:
                prevSums[currSum] = 1

        return ansCount