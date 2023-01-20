from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        for edge in edges:
            edge.sort()
        if not edges:
            if n == 1:
                return True
            else:
                return False
        graph = {}
        for ai, bi in edges:
            graph.setdefault(ai, set()).add(bi)
            graph.setdefault(bi, set()).add(ai)
        queue = [edges[0][0]]
        visited = {edges[0][0]}
        while queue:
            l = len(queue)
            for _ in range(l):
                node = queue.pop(0)
                if graph.get(node):
                    for next_node in graph[node]:
                        if next_node in visited:
                            return False
                        queue.append(next_node)
                        visited.add(next_node)
                        graph[next_node].discard(node)
        if len(visited) == n:
            return True
        return False
