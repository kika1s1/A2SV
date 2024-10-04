class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        ans = 0
        while left <=right:
            area = min(height[right], height[left])*(right-left)
            ans = max(ans, area)
            if height[left] > height[right]:
                right -=1
            else:
                left +=1
        return ans