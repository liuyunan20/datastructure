from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        visited = set()
        a_set = set()
        b_set = set()

        for u in range(n):
            if u not in visited:
                a_set.add(u)
                visited.add(u)
                b_set.update(graph[u])
                while a_set & visited != a_set or b_set & visited != b_set:
                    for v in (b_set ^ visited) & b_set:
                        if v in a_set:
                            return False
                        a_set.update(graph[v])
                        visited.add(v)

                    for u1 in (a_set ^ visited) & a_set:
                        if u1 in b_set:
                            return False
                        b_set.update(graph[u1])
                        visited.add(u1)

        return True
