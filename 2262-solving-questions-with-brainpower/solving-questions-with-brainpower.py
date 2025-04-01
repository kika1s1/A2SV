class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        """

        [[3,2],[4,3],[4,4],[2,5]]
        0      1      2     3
        3 ,2 |   4, 3  | 4, 4, | 2, 5
        create ans = [0]* len(questions)
        start from end and continue adding
        how to add:
            add 4 and nth together 
        return maxim
        """
        N = len(questions)
        maxim = [0] * (N)
        ans = [0] * (N)
        for i in range(N-1, -1, -1):
            if i == N-1:
                ans[i] = questions[i][0]
                maxim[i] = questions[i][1]
                maxim[i] = ans[i]
            else:
                end = i+questions[i][1] +1
                if end >= N:
                    ans[i] = questions[i][0]
                else:
                    ans[i] = questions[i][0] + maxim[end]
                maxim[i] = max(ans[i], maxim[i+1])
        # print(ans)
        # print(maxim)
        return max(ans)

