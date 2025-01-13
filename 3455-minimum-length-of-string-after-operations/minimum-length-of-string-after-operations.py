class Solution:
    def minimumLength(self, s: str) -> int:
        arr = defaultdict(int)
        ans = 0
        for c in s:
            arr[c] +=1
            if arr[c] == 1:
                ans += 1
            elif arr[c] % 2 == 0: 
                ans += 1
            else:
                ans -= 1
        return ans
