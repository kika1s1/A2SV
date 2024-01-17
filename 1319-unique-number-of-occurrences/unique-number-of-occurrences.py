class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        numRep = Counter(arr)
        return len(numRep.values()) ==len(set(numRep.values()))