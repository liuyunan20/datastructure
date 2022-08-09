from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        tree = []
        if not root:
            return []
        tree += self.inorderTraversal(root.left)
        tree.append(root.val)
        tree += self.inorderTraversal(root.right)
        return tree

    def inorderTraversal_2(self, root: Optional[TreeNode]) -> List[int]:
        tree = []
        if not root:
            return
        self.inorderTraversal(root.left)
        tree.append(root.val)
        self.inorderTraversal(root.right)
        return tree
