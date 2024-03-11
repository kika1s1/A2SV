class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        I see leetcode account return median(sorted(nums1 + nums2)) 
        but guys shame on us since it is hard question let try to write a little bit 
        by ourselves \U0001f601\U0001f601
        """
        nums1.extend(nums2)
        nums1.sort()
        # print(nums1)
        if len(nums1)%2 == 1:
            return nums1[len(nums1)//2]
        else:
            # print(nums1[(len(nums1)//2)-1], nums1[len(nums1)//2])
            return ( nums1[(len(nums1)//2)-1] +  nums1[len(nums1)//2])/2