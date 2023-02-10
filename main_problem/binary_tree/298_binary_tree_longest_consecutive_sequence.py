class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestConsecutive_tle(self, root: Optional[TreeNode]) -> int:
        def find_cons_path(node, path):
            if not node:
                return path
            if node.left and node.left.val - node.val == 1:
                path_left = find_cons_path(node.left, path + 1)
            else:
                path_left = path
            if node.right and node.right.val - node.val == 1:
                path_right = find_cons_path(node.right, path + 1)
            else:
                path_right = path
            return max(path, path_left, path_right)
        queue = [root]
        result = 1
        while queue:
            n = queue.pop(0)
            result = max(result, find_cons_path(n, 1))
            if n.left:
                queue.append(n.left)
            if n.right:
                queue.append(n.right)
        return result
