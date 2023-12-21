class Solution:
    def largestGoodInteger(self, num: str) -> str:
        result = ''
        for i in range(len(num)-2):
            if num[i] == num[i+1] == num[i+2]:
                if num[i] > result:
                    result = num[i:i+3]
        return result 