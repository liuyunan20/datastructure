# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        nodes = [root]
        while nodes:
            l = len(nodes)
            level = list(nodes)
            for _ in range(l):
                node = nodes.pop(0)
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
            for i in range(l - 1):
                level[i].next = level[i + 1]
            level[-1].next = None
        return root
