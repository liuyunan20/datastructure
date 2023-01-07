from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre_course = {}
        for pair in prerequisites:
            pre_course.setdefault(pair[0], []).append(pair[1])
        finished = []
        visited = set()
        def bfs(a):
            if a not in pre_course:
                if a not in finished:
                    finished.append(a)
                return True
            if a in finished:
                return True
            if a in visited:
                return False
            visited.add(a)
            for b in pre_course[a]:
                if bfs(b):
                    if b not in finished:
                        finished.append(b)
                else:
                    return False
            finished.append(a)
            visited.discard(a)
            return True
        for ai in range(numCourses):
            if not bfs(ai):
                return []
        return finished
