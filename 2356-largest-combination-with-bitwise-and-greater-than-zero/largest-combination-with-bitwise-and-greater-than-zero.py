class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        bit_similar = [0]*24
        for num in candidates:
            n = bin(num)[2:]
            l  = num.bit_length()
            for index, bit in enumerate(n):
                bit_similar[23-l+1+index] +=int(bit)
        return(max(bit_similar))