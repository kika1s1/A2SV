class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        queue = deque()
        visited = set()
        R, C = len(isWater), len(isWater[0])
        for i in range(R):
            for j in range(C):
                if isWater[i][j] == 1:
                    queue.append((i, j, 0))
                    visited.add((i, j))
                isWater[i][j] = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def inbound(x, y):
            return 0 <=x < R and 0<=y<C
        
        while queue:
            for _ in range(len(queue)):
                x, y, current = queue.popleft()
                for i, j in directions:
                    nr, nc = x+i, y+j
                    if inbound(nr, nc)  and (nr, nc) not in visited:
                        isWater[nr][nc] = current+1
                        visited.add((nr, nc))
                        queue.append((nr, nc, current+1))
        return isWater

