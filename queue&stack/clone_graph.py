class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        def dfs(node, visited):
            if not node:
                return None
            if node not in visited:
                node_clone = Node(node.val)
                visited[node.val] = node_clone
            if not node.neighbors:
                node_clone.neighbors = []
            else:
                for nei in node.neighbors:
                    if nei.val in visited:
                        node_clone.neighbors.append(visited[nei.val])
                    else:
                        node_clone.neighbors.append(dfs(nei, visited))
            return node_clone

        visited = {}
        root = dfs(node, visited)
        return root
