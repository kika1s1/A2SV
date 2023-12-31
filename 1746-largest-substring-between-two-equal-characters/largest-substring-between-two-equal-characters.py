class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        maximum = -1
        for i in s:
            r = s.rindex(i)
            l = s.index(i)+1
            maximum = max(maximum, r-l)
       
        return maximum