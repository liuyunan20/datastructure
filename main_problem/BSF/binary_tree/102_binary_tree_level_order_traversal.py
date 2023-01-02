# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        nodes = [[root]]
        tree = []
        while nodes:
            current_level = nodes.pop(0)
            if not current_level:
                return tree
            current = []
            next_level = []
            for node in current_level:
                current.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            tree.append(current)
            nodes.append(next_level)
