class Solution:
    def nthUglyNumber(self, n: int) -> int:
        primes = {2,3,5}
        heap  =[1]
        seen = {1}
        for i in range(n-1):
            num = heappop(heap)
            for prime in primes:
                if num * prime not in seen:
                    seen.add(num*prime)
                    heappush(heap, num*prime)
        return heappop(heap)