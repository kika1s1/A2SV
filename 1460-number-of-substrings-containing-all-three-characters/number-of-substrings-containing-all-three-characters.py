class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        #tamirat
        dict_cnt={'a':0,'b':0,'c':0}
        n=len(s)
        left=0
        res=0

        for right in range(len(s)):
            dict_cnt[s[right]]+=1
            while(dict_cnt['a'] and dict_cnt['b']  and dict_cnt['c']):
                res+=n-right
                dict_cnt[s[left]]-=1
                left+=1

        return res
        