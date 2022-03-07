# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # solution I thought from level traversal method
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        current_level_nodes = [root]
        level = 0
        while current_level_nodes:
            next_level_nodes = []
            for node in current_level_nodes:
                if node:
                    next_level_nodes.append(node.left)
                    next_level_nodes.append(node.right)
            if next_level_nodes:
                level += 1
            current_level_nodes = next_level_nodes
        return level

    def maxDepth_recursion(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        depth_left = self.maxDepth_recursion(root.left) + 1
        depth_right = self.maxDepth_recursion(root.right) + 1
        return max(depth_left, depth_right)
