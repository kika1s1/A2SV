class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        maxim = max(arr)
        return arr.index(maxim)