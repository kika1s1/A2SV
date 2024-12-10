class Solution:
    def maximumLength(self, s: str) -> int:
        rep = Counter()
        for i in range(len(s)):
            for j in range(i, len(s)):
                sub = s[i:j+1]
                if len(set(sub)) == 1:
                    rep[sub] +=1
        maxim = -1
        for sub, times in rep.items():
            if times >=3:
                maxim = max(maxim, len(sub))
        return maxim