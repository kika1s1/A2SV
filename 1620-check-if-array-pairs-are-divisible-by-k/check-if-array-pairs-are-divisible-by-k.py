class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        freq = [0]*k
        for num in arr:
            num %=k
            freq[num] +=1
        if freq[0]%2 !=0:
            return False
        for i in range(1, (k//2)+1):
            if freq[i] !=freq[k-i]:
                return False
        return True