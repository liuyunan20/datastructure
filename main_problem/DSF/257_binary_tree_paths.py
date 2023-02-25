from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []
        def dfs(path, node):
            if not node:
                return
            if not node.left and not node.right:
                path.append(str(node.val))
                result.append("->".join(path))
                path.pop()
                return
            path.append(str(node.val))
            dfs(path, node.left)
            dfs(path, node.right)
            path.pop()
        dfs([], root)
        return result
