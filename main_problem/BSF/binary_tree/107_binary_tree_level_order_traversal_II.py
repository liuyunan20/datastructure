from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        tree = []
        current_level = [root]
        while current_level:
            current = []
            next_level = []
            for node in current_level:
                current.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            tree.append(current)
            current_level = next_level
        return tree[::-1]
