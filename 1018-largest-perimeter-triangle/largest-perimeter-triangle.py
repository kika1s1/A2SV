class Solution:
    def largestPerimeter(self, arr: List[int]) -> int:
        arr.sort()  # Sort the array in non-decreasing order
        n = len(arr)
        maximum = 0
        for i in range(n - 2):
            a = arr[i]
            b = arr[i + 1]
            c = arr[i + 2]
            if a + b > c:
                if a+b+c > maximum:
                    maximum = a+b+c
                
        return maximum
        