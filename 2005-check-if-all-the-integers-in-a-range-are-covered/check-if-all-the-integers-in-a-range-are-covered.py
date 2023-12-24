class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ranges.sort(key= lambda arr:arr[0])
        left_start=ranges[0][0]
        if left_start > left:
            return False
        for start,end in (ranges):
            if left_start<start-1 and left_start in range(left,right+1):
                return False
            left_start=max(left_start,end)
            if left_start>=right:
                return True
        return False


        