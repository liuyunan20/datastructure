# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)

        current_level_nodes = [root]
        while current_level_nodes:
            next_level_nodes = []
            for node in current_level_nodes:
                if node.val > val and node.left is None:
                    node.left = TreeNode(val)
                    return root
                if node.val < val and node.right is None:
                    node.right = TreeNode(val)
                    return root
                if node.val > val:
                    next_level_nodes.append(node.left)
                if node.val < val:
                    next_level_nodes.append(node.right)
            current_level_nodes = next_level_nodes
