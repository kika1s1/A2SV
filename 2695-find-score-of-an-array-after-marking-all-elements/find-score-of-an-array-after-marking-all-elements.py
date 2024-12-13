class Solution:
    def findScore(self, nums: List[int]) -> int:
        heap = []
        for i, num in enumerate(nums):
            heappush(heap, (num, i))
        visited = set()
        score = 0
        while heap:
            num, index = heappop(heap)
            if index not in visited:
                visited.add(index)
                visited.add(index-1)
                visited.add(index+1)
                score +=num
        return score                 
        
        
