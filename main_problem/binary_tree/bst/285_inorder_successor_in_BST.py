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

    def inorderSuccessor_iterator(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        stack = [root]
        tree = []
        while stack:
            node = stack.pop()
            if not node.left and not node.right:
                if tree and tree[-1] == p.val:
                    return node
                tree.append(node.val)
            else:
                if node.right:
                    stack.append(node.right)
                    node.right = None
                stack.append(node)
                if node.left:
                    stack.append(node.left)
                    node.left = None
