class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        HashMap = {}
        ans = []
        for n in strs:
            name = "".join(sorted(list(n)))

            if name in HashMap:
                HashMap[name].append(n)
            else:
                HashMap[name] = [n]
        for i in HashMap.values():
            ans.append(i)
        return ans
        
            