class Solution:
    def findLHS(self, nums: List[int]) -> int:
      stats = collections.defaultdict(int)
      res = 0
      for n in nums:
        stats[n] += 1
        if n+1 in stats: res = max(res, stats[n+1] + stats[n])
        if n-1 in stats: res = max(res, stats[n-1] + stats[n])
      return res