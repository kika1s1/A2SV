class Solution:
    def minDifficulty(self, jobDifficulty, d):
        len_dif = len(jobDifficulty)
        if len_dif < d:
            return -1
        cache = {}
        def count(index, d, cur_max):
            if index == len_dif:
                return 0 if d == 0 else float("inf")
            if d <= 0:
                return float("inf")
            if (index, d, cur_max) in cache:
                return cache[(index, d, cur_max)]
            res = 0
            cur_max = max(jobDifficulty[index], cur_max)
            res += min(
                cur_max + count(index+1, d-1, -1),
                count(index + 1, d, cur_max)
            )
            cache[(index, d, cur_max)] = res
            return res
        return count(0, d, jobDifficulty[0])