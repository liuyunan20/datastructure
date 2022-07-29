from typing import List


class Solution:
    def canFinish_tle(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # DFS
        ai_bi = {}  # store course: [preceding courses]
        for ai, bi in prerequisites:
            if ai == bi:
                return False
            ai_bi.setdefault(ai, []).append(bi)

        def dfs(course, pres):
            if not ai_bi.get(course):
                return True
            for bi in ai_bi[course]:
                if bi in pres or not dfs(bi, pres + [bi]):
                    return False
            return True
        for ai in ai_bi:
            if not dfs(ai, [ai]):
                return False
        return True
