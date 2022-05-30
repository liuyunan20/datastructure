# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(root):
            if not root:
                return [True, 0]
            left_result = helper(root.left)
            right_result = helper(root.right)
            if left_result[0] and right_result[0] and abs(left_result[1]-right_result[1]) <= 1:
                return True, max(left_result[1], right_result[1]) + 1
            else:
                return False, 0
        result = helper(root)
        return result[0]
