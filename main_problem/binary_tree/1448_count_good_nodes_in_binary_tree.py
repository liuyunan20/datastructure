class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def helper(node, path):
            if not node:
                return 0
            path.append(node.val)
            if node.val >= max(path):
                return helper(node.left, list(path)) + helper(node.right, list(path)) + 1
            return helper(node.left, list(path)) + helper(node.right, list(path))

        return helper(root, [])
