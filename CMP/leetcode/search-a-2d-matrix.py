class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        newArr = []
        for i in matrix:
            newArr.extend(i)
        if target in newArr:
            return True
        else:
            return False