class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        cnt = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                val = words[i]
                if words[j].startswith(val) and words[j].endswith(val):
                    cnt +=1
        return cnt