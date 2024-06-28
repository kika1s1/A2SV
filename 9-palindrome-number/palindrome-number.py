class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        n = x
        cnt = len(str(x))-1
        ans = 0
        while True:
            # print(ans)
            # cnt +=1
            if x%10 == x:
                # print(x)

                ans +=x*(10**cnt)
                print(ans)
                return ans == n
            r = x % 10
            x //=10
            ans +=r*(10**cnt)
            cnt -=1