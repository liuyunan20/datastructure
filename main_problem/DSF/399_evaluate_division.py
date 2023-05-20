from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def dfs(x1, x2, val, visited):
            if x1 == x2:
                return val
            value = -1
            visited.add(x1)
            for x3, v in dic[x1]:
                if x3 not in visited:
                    value = dfs(x3, x2, val * v, visited)
                    if value > 0:
                        return value
            return value

        dic = {}
        for i in range(len(equations)):
            dic.setdefault(equations[i][0], set()).add((equations[i][1], values[i]))
            dic.setdefault(equations[i][1], set()).add((equations[i][0], 1 / values[i]))

        result = []
        for q1, q2 in queries:
            value = 1
            if q1 in dic and q1 == q2:
                result.append(1.0)
                continue
            if q1 not in dic or q2 not in dic:
                result.append(-1.0)
                continue
            value = dfs(q1, q2, 1.0, set())
            result.append(value)

        return result
