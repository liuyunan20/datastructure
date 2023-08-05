# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        result = []
        def help(node):
            if not node:
                return
            if node.left and not node.left.left and not node.left.right:
                result.append(node.left.val)
            help(node.left)
            help(node.right)
        help(root)
        return sum(result)
