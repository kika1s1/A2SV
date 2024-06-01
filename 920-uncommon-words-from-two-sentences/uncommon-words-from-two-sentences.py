class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:

        s_1 = Counter(s1.split())
        s_2 = Counter(s2.split())
        ans = []
        for word in s_1:
            if s_1[word] ==1 and word not in s_2:
                ans.append(word)
        for word in s_2:
            if s_2[word] ==1 and word not in s_1:
                ans.append(word)
        return ans
