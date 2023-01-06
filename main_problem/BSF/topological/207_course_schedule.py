class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_courses = {}
        for pair in prerequisites:
            pre_courses.setdefault(pair[0], []).append(pair[1])
        finished = set()
        visited = set()
        def bfs(a):
            if a not in pre_courses or a in finished:
                return True
            if a in visited:
                return False
            visited.add(a)
            for b in pre_courses[a]:
                if bfs(b):
                    finished.add(b)
                else:
                    return False
            visited.discard(a)
            return True

        for ai in pre_courses:
            if not bfs(ai):
                return False
        return True
