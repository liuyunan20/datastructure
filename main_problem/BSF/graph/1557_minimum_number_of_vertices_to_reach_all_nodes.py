from typing import List


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        result = set(range(n))
        dependent = set()
        for pre, node in edges:
            dependent.add(node)
        return result - dependent
