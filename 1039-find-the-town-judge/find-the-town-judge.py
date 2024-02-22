class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1
        candidates = set()
        anti_candidates = set()
        trust_counter = [0] * n
        for t, t1 in trust:
            trust_counter[t1-1] += 1
            anti_candidates.add(t)
            if trust_counter[t1-1] == n-1:
                candidates.add(t1)
        candidates = candidates.difference(anti_candidates)
        return candidates.pop() if candidates else -1