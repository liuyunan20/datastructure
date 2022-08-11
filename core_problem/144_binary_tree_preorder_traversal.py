# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal_recursion(self, root: Optional[TreeNode]) -> List[int]:
        tree = []
        if not root:
            return []
        tree.append(root.val)
        tree += self.preorderTraversal(root.left)
        tree += self.preorderTraversal(root.right)
        return tree

    def preorderTraversal_iteration(self, root: Optional[TreeNode]) -> List[int]:
        tree = []
        stack = []
        while root:
            tree.append(root.val)
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)
            if not stack:
                break
            root = stack.pop()
        return tree
