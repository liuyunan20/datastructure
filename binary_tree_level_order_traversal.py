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
        my_stack = [[root]]
        while my_stack:
            current_level = []
            next_level_nodes = []
            for node in my_stack.pop():
                if node:
                    current_level.append(node.val)
                    next_level_nodes.append(node.left)
                    next_level_nodes.append(node.right)
            if next_level_nodes:
                my_stack.append(next_level_nodes)
            if current_level:
                levelorder_tree.append(current_level)
        return levelorder_tree
