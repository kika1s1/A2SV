class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res = Counter(words[0])
        for i in words:
            res &= Counter(i)
        return list(res.elements())
        