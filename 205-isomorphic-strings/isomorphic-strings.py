class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hashmap = {}
        for i in range(len(s)):
            if s[i] in hashmap:
                if hashmap[s[i]] != t[i]:
                    return False
            else:
                hashmap[s[i]] = t[i]
				
         # For few tricky edge cases      
        if len(set(hashmap.values())) != len(hashmap.values()): 
            return False    
        return True
		
        