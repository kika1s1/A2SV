class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        current_position = 1
        direction = 1 
        for _ in range(1,time+1):
            current_position += direction
            if current_position == 1 or current_position == n :
                direction = -direction
        
        return current_position