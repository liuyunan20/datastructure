from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        inorder_tree = []
        if root:
            inorder_tree += self.inorderTraversal(root.left)
            inorder_tree.append(root.val)
            inorder_tree += self.inorderTraversal(root.right)
        return inorder_tree
