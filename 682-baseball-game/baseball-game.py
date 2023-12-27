class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        ans = []
        for i in operations:
            if i.isnumeric():
                ans.append(int(i))
            if i.startswith('-'):
                    ans.append(eval(i))
            elif i == "C":
                ans.pop()
            elif i == "D":
                ans.append(2*ans[-1])
            elif i == "+":
                ans.append((ans[-1])+(ans[-2]))
        return sum(ans)
