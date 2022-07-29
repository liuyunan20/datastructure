from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # BFS solution
        course_step = {}  # store how many preceding courses needed for every course
        bi_ai = {}  # store course and its following courses
        queue = []
        course0 = set()  # store courses without preceding courses
        # if there is no limit for courses, return True
        if not prerequisites:
            return True
        # initialize course_step and bi_ai
        for ai, bi in prerequisites:
            if ai == bi:
                return False
            course_step.setdefault(ai, 0)
            course_step[ai] += 1
            bi_ai.setdefault(bi, []).append(ai)
        # find out initial courses without preceding courses
        for ai, bi in prerequisites:
            if bi not in course_step:
                course0.add(bi)
        # if there's no initial courses, return False
        if not course0:
            return False
        # start BFS searching, find out all courses with 1 preceding course, then 2, 3...
        # until no following courses could be found
        for course in course0:
            queue.append(course)
        while queue:
            bi = queue.pop(0)
            if bi_ai.get(bi):
                for ai in bi_ai[bi]:
                    course_step[ai] -= 1
                    if course_step[ai] == 0:
                        queue.append(ai)
        # check whether there is course which still needs preceding courses, yes return False
        for course in course_step:
            if course_step[course] > 0:
                return False
        return True

# DFS solution, using recursion, but time limit exceed
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
