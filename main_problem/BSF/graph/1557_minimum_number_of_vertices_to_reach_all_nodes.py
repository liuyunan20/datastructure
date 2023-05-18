from typing import List


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        dependent = set()
        for pre, node in edges:
            dependent.add(node)
        result = set()
        for i in range(n):
            if i not in dependent:
                result.add(i)
        return result
