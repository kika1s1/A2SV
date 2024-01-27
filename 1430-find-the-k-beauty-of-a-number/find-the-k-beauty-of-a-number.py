class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        ws = k
        num = str(num)
        l = 0
        cnt = 0

        for i in range(len(num)-(ws-1)):
            sub = num[i:k+i]
            if int(sub) == 0:
                continue
            elif int(num) % int(sub) == 0:
                cnt +=1
        return cnt

        