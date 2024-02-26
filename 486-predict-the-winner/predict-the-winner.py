class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n=len(nums)
        @lru_cache(None)
        def dp(i,j):
            return 0 if i>j else max(-dp(i+1,j)+nums[i],-dp(i,j-1)+nums[j])

        return dp(0,n-1)>=0