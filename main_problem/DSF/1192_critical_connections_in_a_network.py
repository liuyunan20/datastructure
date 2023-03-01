from typing import List


class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        path_memo = {}
        graph = {}
        for ai, bi in connections:
            graph.setdefault(ai, set()).add(bi)
            graph.setdefault(bi, set()).add(ai)

        def traversal(p1):
            queue = [p1]
            visited = {p1,}
            while queue:
                node = queue.pop()
                for nei in graph[node]:
                    if nei not in visited:
                        queue.append(nei)
                        visited.add(nei)
            if len(visited) == n:
                return True
            return False

        result = []
        for ai, bi in connections:
            graph[ai].discard(bi)
            graph[bi].discard(ai)
            if not traversal(ai):
                result.append([ai, bi])
            graph[ai].add(bi)
            graph[bi].add(ai)
        return result
