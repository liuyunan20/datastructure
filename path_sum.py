# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root:
            if root.left is None and root.right is None:
                if root.val == targetSum:
                    return True
            else:
                targetSum -= root.val
                if self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum):
                    return True
        return False
