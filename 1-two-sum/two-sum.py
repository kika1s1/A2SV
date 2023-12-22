class Solution:
      def binary_search(self, xs, x, lo=0, hi=None):
        while True:
          if lo >= hi:
              return None
          mid = (lo + hi) // 2
          if xs[mid][0] == x:
              return mid
          elif xs[mid][0] > x:
              hi = mid
          else:
              lo = mid+1
                
      def twoSum(self, nums, target):
        sort = sorted((n,i) for i,n in enumerate(nums))
        for i in range(len(sort)):
          if j := self.binary_search(sort, target-sort[i][0], i, len(sort)):
             return [sort[i][1], sort[j][1]]