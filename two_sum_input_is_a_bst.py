# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        current_level = [root]
        tree_value = []

        while current_level:
            next_level = []
            for node in current_level:
                if node:
                    tree_value.append(node.val)
                    next_level.append(node.left)
                    next_level.append(node.right)
            current_level = next_level
        sub = []
        for value in tree_value:
            if value in sub:
                return True
            sub.append(k - value)
        return False
