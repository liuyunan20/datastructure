# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def deepth(node, d):
            if not node:
                return d
            return max(deepth(node.left, d), deepth(node.right, d)) + 1
        nodes = [root]
        result = 0
        while nodes:
            node = nodes.pop(0)
            result = max(result, deepth(node.left, 0) + deepth(node.right, 0))
            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)
        return result
