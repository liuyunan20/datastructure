from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def get_value(q1, q2, visited, v):
            if q1 == q2:
                return (True, v)
            for letter, val in maps[q1]:
                if letter in visited:
                    continue
                visited.append(letter)
                find, value = get_value(letter, q2, list(visited), v * val)
                if find:
                    return (find, value)
            return (False, -1)

        n = len(equations)
        maps = {}
        for i in range(n):
            maps.setdefault(equations[i][0], []).append((equations[i][1], values[i]))
            maps.setdefault(equations[i][1], []).append((equations[i][0], 1 / values[i]))
        result = []
        for q1, q2 in queries:
            if q1 not in maps or q2 not in maps:
                result.append(-1)
            else:
                find, value = get_value(q1, q2, [], 1)
                if find:
                    result.append(value)
                else:
                    result.append(-1)
        return result
