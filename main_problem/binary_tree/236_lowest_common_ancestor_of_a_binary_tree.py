class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        values = (p.val, q.val)
        result = []

        def helper(node):
            if not node:
                return False
            if node.val in values:
                mid = True
            else:
                mid = False
            left = helper(node.left)
            right = helper(node.right)
            if (mid and left) or (mid and right) or (left and right):
                result.append(node)
            return mid or left or right

        helper(root)
        return result[0]
