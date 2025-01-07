class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = []
        for index, word in enumerate(words):
            for j, char in enumerate(words):
                if index != j and word in char:
                    ans.append(word)
                    break
                
        return ans            