class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        reversed_s = s[::-1]
        new_s = s + "#" + reversed_s
        prefix_suffix = self.calculatePrefixSuffix(new_s)
        palindrome_prefix_len = prefix_suffix[-1]
        return reversed_s[:len(s) - palindrome_prefix_len] + s
    def calculatePrefixSuffix(self, s: str) -> List[int]:
        n = len(s)
        prefix_suffix = [0] * n
        length = 0
        i = 1
        while i < n:
            if s[i] == s[length]:
                length += 1
                prefix_suffix[i] = length
                i += 1
            else:
                if length != 0:
                    length = prefix_suffix[length - 1]
                else:
                    prefix_suffix[i] = 0
                    i += 1
        return prefix_suffix