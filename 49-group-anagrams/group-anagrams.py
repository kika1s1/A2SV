class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        dictAnagram = {}
        for anagram in strs:
            b = "".join(sorted(anagram))
            if b not in dictAnagram:
                dictAnagram[b] = [anagram]
            else:
                arr = dictAnagram[b]
                arr.append(anagram)

        ans = []
        for i in dictAnagram.values():
            ans.append(i)
        return ans