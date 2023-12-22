class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        count = 0
        right = 0
        Cap = capacity
        while right<len(plants):
            if plants[right]<=Cap:
              Cap -=plants[right]
              count+=1
              right+=1
            else:
              Cap =  capacity  -plants[right]
              count+=2*right +1
              right+=1
        return count
        