class Solution(object):
    def largestPerimeter(self, A):
        A.sort(reverse=True)

        for i in range(len(A)-2):
            a = A[i]
            b= A[i+1]
            c = A[i+2]
            if a< b+ c:
                return a+b+c
            
        return 0