class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        incoming_edge = [0] * numCourses
        for course, pre in prerequisites:
            graph[pre].append(course)
            incoming_edge[course] +=1
        visited = set()
        ans = []
        queue = deque()
        for index in range(len(incoming_edge)):
            if incoming_edge[index] == 0:
                queue.append(index)
        while queue:
            node = queue.popleft()
            visited.add(node)
            ans.append(node)
            for nei in graph[node]:
                incoming_edge[nei] -=1
                if nei not in visited and incoming_edge[nei] == 0:
                    queue.append(nei)
        if len(visited) == numCourses:
            return ans
        return []
