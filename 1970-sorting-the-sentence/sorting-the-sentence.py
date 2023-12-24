class Solution:
    def sortSentence(self, s: str) -> str:
        ans = [x for x in s.split()]
        # place
        for i in s.split():
            place = int(i[-1])-1
            ans[place] = i[:-1]
        return " ".join(ans)