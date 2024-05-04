class Solution:
    def fib(self, n: int) -> int:
        def fibonacci(n, memo):
            if n < 2:
                return n
            if n not in memo:
                memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
            return memo[n]
        memo = {}
        return fibonacci(n, memo)