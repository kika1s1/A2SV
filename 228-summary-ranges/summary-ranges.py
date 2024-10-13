class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        N = len(nums)
        if N <=1:
            return [str(x) for x in nums] 
        l, r = 0, 1
        prev = nums[0]
        while l < r < N:
            if nums[l]+1 == nums[r]:
                l +=1
                r +=1
            else:
                if nums[l] == prev:
                    ans.append(str(prev))
                    prev = nums[l+1]
                else:
                    ans.append(f"{prev}->{nums[l]}")
                    prev = nums[l+1]
                l +=1
                r +=1
        if prev == nums[N-1]:
            ans.append(str(prev))
        else:
            ans.append(f"{prev}->{nums[N-1]}")
            

        return ans