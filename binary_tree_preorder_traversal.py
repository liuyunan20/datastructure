from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        preorder_tree = []
        if root:
            preorder_tree.append(root.val)
            preorder_tree += self.preorderTraversal(root.left)
            preorder_tree += self.preorderTraversal(root.right)
        return preorder_tree
