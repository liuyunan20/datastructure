# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levelorder_tree = []
        current_level_nodes = [root]
        while current_level_nodes:
            current_level = []
            next_level_nodes = []
            for node in current_level_nodes:
                if node:
                    current_level.append(node.val)
                    next_level_nodes.append(node.left)
                    next_level_nodes.append(node.right)
            current_level_nodes = next_level_nodes
            if current_level:
                levelorder_tree.append(current_level)
        return levelorder_tree
