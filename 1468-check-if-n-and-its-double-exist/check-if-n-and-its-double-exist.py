class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i in range(len(arr)):
            double = arr[i]*2
            if double in arr and arr.index(double) != i:
                return True
        return False