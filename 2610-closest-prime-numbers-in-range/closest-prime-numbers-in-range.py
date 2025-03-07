class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        is_primes = [True for i in range((right) + 1) ]
        is_primes[0] = False
        is_primes[1] = False
        for i in range(2, int(right ** 0.5) +1):
            if is_primes[i]:
                for j in range(i*i, right+1, i):
                    is_primes[j] = False
        primes = [i for i in range(left, right + 1) if is_primes[i]]
        ans = [-1, -1]
        diff = float("inf")
        for i in range(1, len(primes)):
            if primes[i] - primes[i-1] < diff:
                diff = primes[i] - primes[i-1]
                ans = [primes[i-1], primes[i]]
        return ans
