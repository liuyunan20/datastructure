# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder_tree(root):
            tree = []
            if not root:
                return tree
            tree += inorder_tree(root.left)
            tree.append(root.val)
            tree += inorder_tree(root.right)
            return tree
        inorder = inorder_tree(root)
        return inorder[k-1]
