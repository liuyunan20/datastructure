# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor_1(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while True:
            if root.val > max(p.val, q.val):
                root = root.left
                continue
            if root.val < min(p.val, q.val):
                root = root.right
                continue
            else:
                return root

    # use recursion
    def lowestCommonAncestor_2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if min(p.val, q.val) <= root.val <= max(p.val, q.val):
            return root
        if root.val > max(p.val, q.val):
            return self.lowestCommonAncestor_2(root.left, p, q)
        if root.val < min(p.val, q.val):
            return self.lowestCommonAncestor_2(root.right, p, q)
