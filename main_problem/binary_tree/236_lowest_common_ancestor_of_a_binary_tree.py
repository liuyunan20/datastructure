class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor_tle(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def find_p(node, target):
            if not node:
                return False
            if node == target:
                return True
            return find_p(node.left, target) or find_p(node.right, target)

        node = root
        while node:
            if find_p(node.left, p) and find_p(node.left, q):
                node = node.left
            elif find_p(node.right, p) and find_p(node.right, q):
                node = node.right
            else:
                return node
