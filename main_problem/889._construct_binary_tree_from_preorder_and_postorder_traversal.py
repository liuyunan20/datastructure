# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder and not postorder:
            return None

        root = TreeNode()
        root.val = preorder[0]
        if len(preorder) == 1:
            return root

        idx = postorder.index(preorder[1])
        left_postorder = postorder[: idx + 1]
        right_postorder = postorder[idx + 1: len(postorder) - 1]
        left_preorder = preorder[1: len(left_postorder) + 1]
        right_preorder = preorder[len(left_postorder) + 1:]

        root.left = self.constructFromPrePost(left_preorder, left_postorder)
        root.right = self.constructFromPrePost(right_preorder, right_postorder)

        return root
