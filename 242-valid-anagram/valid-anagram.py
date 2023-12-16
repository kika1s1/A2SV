class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = Counter(s)
        b = Counter(t)
        return a ==b
            