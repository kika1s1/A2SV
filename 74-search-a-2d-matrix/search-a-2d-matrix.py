class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r, c = len(matrix), len(matrix[0])
        left, right  =0,  r * c -1
        while left <= right:
            mid = (left+right)//2
            i, j = mid//c, mid % c
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                left = mid+1
            else:
                right = mid -1
        return False
