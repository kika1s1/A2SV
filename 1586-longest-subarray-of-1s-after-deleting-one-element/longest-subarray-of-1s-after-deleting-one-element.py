# class Solution:
#     def longestSubarray(self, nums: List[int]) -> int:
#         maxim = float("-inf")
#         for i in range(len(nums)):
#             cnt = 0
#             for j in range(len(nums)):
#                 if j == i:
#                     continue
#                 elif nums[j] == 1:
#                     cnt += 1
#                     maxim = max(maxim, cnt)
#                 else:
#                     cnt = 0

#                     maxim = max(maxim, cnt)

#         return maxim

# class Solution:
#     def longestSubarray(self, nums: List[int]) -> int:
#         prev=0
#         count=0
#         ls=[]
#         visit=False
#         for i in nums:
#             if i==0:
#                 visit=True
#                 ls.append(prev+count)
#                 prev=count
#                 count=0
#             if i==1:
#                 count+=1
#         if not visit:
#             count-=1
#         ls.append(count+prev)
#         return max(ls)

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        r=l=0
        k=1

        for r in range(len(nums)):
            if nums[r]==0:
                k -=1
            if k<0:
                if nums[l] == 0:
                    k+=1
                
                l+=1
        
        return r-l