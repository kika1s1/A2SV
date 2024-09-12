class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def combine(left, right):
            m = len(left)
            n = len(right)
            i, j = 0, 0
            combined = []
            while i < m and j < n:
                if left[i] < right[j]:
                    combined.append(left[i])
                    i +=1
                else:
                    combined.append(right[j])
                    j +=1
            combined.extend(left[i:])
            combined.extend(right[j:])
            return combined
        def mergeSort(arr):
            if len(arr) <=1:
                return arr
            mid = len(arr)//2
            left = mergeSort(arr[:mid])
            right = mergeSort(arr[mid:])
            return combine(left, right)
        return mergeSort(nums)
        
