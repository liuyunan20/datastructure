from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = [root]
        visited = set()
        while k > 0:
            root = stack.pop()
            while root not in visited and (root.left or root.right):
                if root.right:
                    stack.append(root.right)
                stack.append(root)
                if root.left:
                    stack.append(root.left)
                visited.add(root)
                root = stack.pop()
            k -= 1
        return root.val
