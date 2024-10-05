class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        cnt = defaultdict(int)
        N = len(s1)
        cnt1 = Counter(s1)
        l = 0
        for i in range(len(s2)):
            if i < N:
                cnt[s2[i]] +=1
                if cnt1 == cnt:
                    return True
            elif cnt1 == cnt:
                return True
            else:
                if cnt[s2[l]]>1:
                    cnt[s2[l]] -=1
                elif cnt[s2[l]] == 1:
                    del cnt[s2[l]]
                cnt[s2[i]] +=1
                l +=1
                if cnt1 == cnt:
                    return True
        return False
