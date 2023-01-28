from typing import Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        def get_left_leave(node):
            while node.left:
                node = node.left
            return node


        def get_next(node, p, result):
            if node.val == p.val:
                if node.right:
                    return get_left_leave(node.right)
                else:
                    return result
            if node.val > p.val:
                return get_next(node.left, p, node)
            if node.val < p.val:
                return get_next(node.right, p, result)
        return get_next(root, p, None)
