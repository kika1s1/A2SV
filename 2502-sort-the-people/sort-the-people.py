class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        N = len(names)
        for i in range(N):
            for j in range(N-i-1):
                if heights[j] < heights[j+1]:
                    names[j], names[j+1] = names[j+1], names[j]
                    heights[j], heights[j+1] = heights[j+1], heights[j]
        return names


