class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        I see leetcode account return median(sorted(nums1 + nums2)) 
        but guys shame on us since it is hard question let try to write a little bit 
        by ourselves \U0001f601\U0001f601
        """
        both = nums1+nums2
        both.sort()
        # print(both)
        if len(both)%2 == 1:
            return both[len(both)//2]
        else:
            # print(both[(len(both)//2)-1], both[len(both)//2])
            return ( both[(len(both)//2)-1] +  both[len(both)//2])/2