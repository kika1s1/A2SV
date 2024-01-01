class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)  
        
        hIndex = 0 
        
        for i in range(len(citations)):
            if citations[i] >= i + 1:
                hIndex += 1
            else:
                break
        
        return hIndex