# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        root = TreeNode()
        root.val = preorder[0]
        left_inorder = inorder[: inorder.index(preorder[0])]
        left_preorder = preorder[1: len(left_inorder) + 1]
        root.left = self.buildTree(left_preorder, left_inorder)
        right_inorder = inorder[inorder.index(preorder[0]) + 1:]
        right_preorder = preorder[len(left_inorder) + 1:]
        root.right = self.buildTree(right_preorder, right_inorder)
        return root
