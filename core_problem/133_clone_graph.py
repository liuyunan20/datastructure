"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return []
        nodes = {}
        visited = set()
        queue = [node]
        while queue:
            node = queue.pop(0)
            nodes[node.val] = Node(node.val)
            for nei in node.neighbors:
                if nei not in nodes:
                    nodes[nei] = Node(nei)
                if nei not in visited:
                    nodes[node.val].neighbors.append(nodes[nei].val)
                    queue.append(nei)
            visited.add(node)
        return nodes.values()
