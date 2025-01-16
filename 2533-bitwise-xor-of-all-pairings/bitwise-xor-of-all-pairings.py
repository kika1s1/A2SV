class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        len1, len2 = len(nums1), len(nums2)
        freq = defaultdict(int)
        for num in nums1:
            freq[num] +=len2
        for num in nums2:
            freq[num] += len1
        ans = 0
        for num in freq:
            if freq[num] % 2:
                ans ^= num

        return ans