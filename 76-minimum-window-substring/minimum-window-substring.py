class Solution:
    def minWindow(self, s: str, t: str) -> str:
        best = len(s)+1
        start = -1
        left = 0
        count_t = Counter(t)
        count_s = Counter()
        for index in range(len(s)):
            count_s[s[index]] +=1
            while count_s >= count_t:
                length = index - left+1
                if length < best:
                    start = left
                    best = length
                count_s[s[left]] -=1
                left +=1
        if start == -1:
            return ""
        print(start, best)
        return s[start:start+best]
