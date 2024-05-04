class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        def find_diff(i, j):
            num = nums1.copy()
            num[i] = "inf"
            num[j] = "inf"
            num.remove("inf")
            num.remove("inf")
            diff = nums2[0]-num[0]
            for a, b in zip(num,nums2):
                if diff !=b-a:
                    return float("inf")
            return diff

        nums1.sort()
        nums2.sort()
        minim = float("inf")
        for i in range(len(nums1)):
            for j in range(i+1, len(nums1)):
                minim = min(minim, find_diff(i, j))
        return minim