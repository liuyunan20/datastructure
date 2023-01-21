from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {}
        for ai, bi in edges:
            graph.setdefault(ai, set()).add(bi)
            graph.setdefault(bi, set()).add(ai)

        count = 0
        visited = set()
        queue = []
        for node in range(n):
            if node not in visited:
                queue.append(node)
                count += 1
            while queue:
                cur_node = queue.pop(0)
                if graph.get(cur_node):
                    for next_node in graph[cur_node]:
                        if next_node not in visited:
                            queue.append(next_node)
                            visited.add(next_node)
        return count
