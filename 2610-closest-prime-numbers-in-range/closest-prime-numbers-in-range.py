class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        if right < 2: 
            return [-1, -1]

        limit = int(right ** 0.5) + 1
        is_prime = [True] * (right + 1)
        is_prime[0] = is_prime[1] = False

        for i in range(2, limit):
            if is_prime[i]:
                for j in range(i * i, right + 1, i):
                    is_prime[j] = False

        primes = [i for i in range(left, right + 1) if is_prime[i]]
        
        if len(primes) < 2:
            return [-1, -1]

        ans = [primes[0], primes[1]]
        min_diff = ans[1] - ans[0]

        for i in range(1, len(primes) - 1):
            diff = primes[i + 1] - primes[i]
            if diff < min_diff:
                min_diff = diff
                ans = [primes[i], primes[i + 1]]
                if min_diff == 2: 
                    break

        return ans
