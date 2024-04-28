class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even = []
        odd = []
        for i in nums:
            if i % 2 ==0:
                even.append(i)
            else:
                odd.append(i)
        ans = []
        even.sort()
        odd.sort()
        odd_cnt = 0
        even_cnt = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                ans.append(even[even_cnt])
                even_cnt +=1
            else:
                ans.append(odd[odd_cnt])
                odd_cnt +=1
        return ans
        