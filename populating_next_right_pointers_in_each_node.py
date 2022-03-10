from typing import Optional


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        current_level = [root]
        while current_level:
            next_level = []
            for i, node in enumerate(current_level):
                if i < len(current_level) - 1:
                    node.next = current_level[i + 1]
                else:
                    node.next = None
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            current_level = next_level
        return root
