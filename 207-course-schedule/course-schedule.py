from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        in_degree = [0] * numCourses

        # Construct the graph and calculate in-degrees
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1

        # Initialize a queue with courses having no prerequisites
        queue = deque(course for course in range(numCourses) if in_degree[course] == 0)
        completed_courses = 0

        # Topological sorting
        while queue:
            course = queue.popleft()
            completed_courses += 1

            # Decrease in-degree of adjacent courses
            for next_course in graph[course]:
                in_degree[next_course] -= 1
                # If in-degree becomes 0, add to queue
                if in_degree[next_course] == 0:
                    queue.append(next_course)

        # If all courses can be completed, return True
        return completed_courses == numCourses
