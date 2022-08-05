"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        visited = set()
        old_new = {}
        if not node:
            return None

        def dfs(n):
            if n in visited:
                return old_new[n]
            visited.add(n)
            new_node = Node()
            old_new[n] = new_node
            new_node.val = n.val
            if n.neighbors:
                new_node.neighbors = []
                for nei in n.neighbors:
                    new_nei = dfs(nei)
                    new_node.neighbors.append(new_nei)
            return new_node

        return dfs(node)
