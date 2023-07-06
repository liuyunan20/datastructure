from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def helper(node, path):
            if not node:
                return 0
            path.append(node.val)
            counter = 0
            for i in range(len(path)):
                if sum(path[i:]) == targetSum:
                    counter += 1
            return helper(node.left, list(path)) + helper(node.right, list(path)) + counter
        return helper(root, [])
