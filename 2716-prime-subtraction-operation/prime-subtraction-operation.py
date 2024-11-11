class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        n  = 1000
        prime = [True for i in range(n+1)]
        p = 2
        while (p * p <= n):
            if (prime[p] == True):
                for i in range(p * p, n+1, p):
                    prime[i] = False
            p += 1
        primes = [p for p in range(2, n) if prime[p]]
        ans = []
        for num in nums:
            l, r = 0, bisect_left(primes, num)-1
            if num == 1:
                if ans and ans[-1] ==1:
                    return False
                ans.append(num)
                continue
            
            if not ans:
                if num == 2:
                    ans.append(2)
                    continue
                ans.append(num-primes[r])
                continue
            best = 0
            while l <=r:
                mid = (l+r)//2
                if num - primes[mid]  == ans[-1]:
                    r = mid - 1
                elif num - primes[mid]  > ans[-1]:
                    best = mid
                    l = mid +1
                else:
                    r = mid-1
                    
            if num - primes[best] <= ans[-1] and ans[-1] >= num:
                return False
            

            ans.append(num if num - primes[best] <= ans[-1] else num - primes[best])
        return ans == sorted(ans)
        
