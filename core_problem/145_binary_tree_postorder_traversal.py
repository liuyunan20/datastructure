# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal_recursion(self, root: Optional[TreeNode]) -> List[int]:
        tree = []
        if root:
            tree += self.postorderTraversal(root.left)
            tree += self.postorderTraversal(root.right)
            tree.append(root.val)
        return tree

    def postorderTraversal_iteratively(self, root: Optional[TreeNode]) -> List[int]:
        tree = []
        stack = [root]
        visited = set()
        if not root:
            return tree
        while stack:
            root = stack.pop()
            while root not in visited and (root.left or root.right):
                stack.append(root)
                if root.right:
                    stack.append(root.right)
                if root.left:
                    stack.append(root.left)
                visited.add(root)
                root = stack.pop()
            tree.append(root.val)
        return tree
