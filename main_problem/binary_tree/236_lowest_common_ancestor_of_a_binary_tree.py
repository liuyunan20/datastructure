class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.lowest = None
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def helper(node):
            if not node:
                return False
            mid = True if node.val in [p.val, q.val] else False
            left = helper(node.left)
            right = helper(node.right)
            if (mid and left) or (mid and right) or (left and right):
                self.lowest = node
            return mid or left or right
        helper(root)
        return self.lowest
