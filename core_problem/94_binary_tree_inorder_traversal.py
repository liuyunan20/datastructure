from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal_recursion(self, root: Optional[TreeNode]) -> List[int]:
        tree = []
        if not root:
            return []
        tree += self.inorderTraversal(root.left)
        tree.append(root.val)
        tree += self.inorderTraversal(root.right)
        return tree

    def inorderTraversal_stack(self, root: Optional[TreeNode]) -> List[int]:
        tree = []
        stack = [root]
        visited = set()
        if not root:
            return tree
        while stack:
            root = stack.pop()
            while root not in visited and (root.left or root.right):
                if root.right:
                    stack.append(root.right)
                stack.append(root)
                visited.add(root)
                if root.left:
                    stack.append(root.left)
                root = stack.pop()
            if (not root.left and not root.right) or root in visited:
                tree.append(root.val)
        return tree
