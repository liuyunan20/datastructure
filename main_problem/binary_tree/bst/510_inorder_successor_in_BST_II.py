class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Optional[Node]':
        if node.right:
            node = node.right
            while node.left:
                node = node.left
            return node
        elif not node.parent:
            return node.parent
        elif node.parent.val > node.val:
            return node.parent
        elif node.parent.val < node.val:
            result = node.parent
            while result.parent and result.parent.val < node.val:
                result = result.parent
            return result.parent
