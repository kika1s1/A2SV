class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = set()
        maxim = 0
        l, r = 0, 0
        length = len(s)

        while r < length:
            if s[r] not in visited:
                visited.add(s[r])
                r += 1
                maxim = max(maxim, r - l)
            else:
                visited.discard(s[l])
                l += 1

        return maxim
