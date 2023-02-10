class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:

        def find_cons_path(node, path):
            if not node:
                return path
            if node.left and node.left.val - node.val == 1:
                path_left = find_cons_path(node.left, path + 1)
            else:
                path_left = find_cons_path(node.left, 1)
            if node.right and node.right.val - node.val == 1:
                path_right = find_cons_path(node.right, path + 1)
            else:
                path_right = find_cons_path(node.right, 1)
            path = max(path, path_left, path_right)
            return path

        return find_cons_path(root, 1)
