class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        mod = 10**9 + 7
        odd = defaultdict(int)
        even = defaultdict(int)
        ans = 0
        for i in range(1, len(arr)):
            arr[i] = arr[i-1] + arr[i]
        for index, num in enumerate(arr):
            ans %=mod
            if num % 2 == 0:
                even[index] +=even[index-1] +1
                odd[index] = odd[index-1]
                ans +=(odd[index])
            else:
                odd[index] +=odd[index-1] +1
                even[index] = even[index-1]
                ans +=(even[index]+1)
        return ans % mod
            
