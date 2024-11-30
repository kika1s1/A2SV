class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        heap = []
        for name, height in zip(names, heights):
            heappush(heap, (-height, name))
        ans = []
        while heap:
            height, name = heappop(heap)
            ans.append(name)
        return ans