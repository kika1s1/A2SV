class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        res  = ""
        for i in s:
            if i.isalpha() or i.isnumeric():
                res +=i
        
        return res.lower() == res[::-1].lower()
        