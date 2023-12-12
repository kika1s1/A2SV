class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxArr = []
        totalSum = 0
        maximum = 0
        allNegative = True
        for i in nums:
            if len(maxArr) == 0 and i <= 0:
                continue
            else:

                if i > 0:
                    allNegative = False
                    maxArr.append(i)
                    totalSum +=i
                    maximum = max(maximum, totalSum)
                else:
                    if totalSum + i <= 0:
                        maxArr.clear()
                        totalSum = 0
                    else:
                        maxArr.append(i)
                        totalSum +=i

        if allNegative:
            maximum = max(nums)
        return maximum

