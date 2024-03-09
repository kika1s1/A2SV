class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        l1, l2 = 0 , 0
        while l1 < len(nums1) and l2 < len(nums2):
            if nums1[l1] == nums2[l2]:
                return nums1[l1]
            elif nums1[l1] > nums2[l2]:
                l2 +=1
            else:
                l1 +=1
        return -1
                