from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        nodes = [root]
        level = 1
        result = 1, root.val
        level_node = []
        while nodes:
            l = len(nodes)
            for _ in range(l):
                node = nodes.pop(0)
                level_node.append(node.val)
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
            new = sum(level_node)
            if  new > result[1]:
                result = level, new
            level_node = []
            level += 1
        return result[0]
