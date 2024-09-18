class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        in_degrees = [0] * numCourses
        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            in_degrees[course] +=1
        queue = deque()
        for course in range(numCourses):
            if in_degrees[course] == 0:
                queue.append(course)
        order = []
        while queue:
            prerequisite = queue.popleft()
            order.append(prerequisite)
            for course in graph[prerequisite]:
                in_degrees[course] -=1
                if in_degrees[course] == 0:
                    queue.append(course)
        if len(order) != numCourses:
            return []
        return order
                
