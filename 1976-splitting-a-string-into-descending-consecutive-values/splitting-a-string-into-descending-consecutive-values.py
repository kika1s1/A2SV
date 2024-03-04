class Solution:
    def splitString(self, s: str) -> bool:
        def backtrack(low, lastNum):
            for i in range(low, len(s)-1):
                split = int(s[low: i+1]);
                if (lastNum == '#' or lastNum-1 == split):
                    if backtrack(i+1, split):
                        return True;
            if lastNum != '#' and int(s[low:]) == lastNum - 1:
                return True;
            return False;
        return backtrack(0, '#');