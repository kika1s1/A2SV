class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ans = []
        only = Counter()
        rep = Counter(s)
        l = 0
        for r in range(len(s)):
            if s[r] not in only:
                only[s[r]] = rep[s[r]]
            only[s[r]] -=1
            if only[s[r]] ==0:
                del only[s[r]]
            if len(only) == 0:
                ans.append(r-l+1)
                l = r+1
        return ans