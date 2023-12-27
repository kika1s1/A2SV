class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        matches = {")": "(", "]": "[", "}": "{"}

        if len(s) < 2 or s[0] in matches:
            return False

        stack = []

        for bracket in s:
            if bracket in "([{":
                stack.append(bracket)
                continue

            if len(stack) <= 0:
                return False

            if stack[-1] == matches[bracket]:
                stack.pop()
            else:
                return False

        if len(stack) == 0:
            return True
        else:
            return False
        