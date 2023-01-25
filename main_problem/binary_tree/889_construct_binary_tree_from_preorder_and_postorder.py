# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        val = preorder[0]
        root = TreeNode(val)
        if len(preorder) == 1:
            return root
        idx = postorder.index(preorder[1])
        left_post = postorder[: idx+1]
        right_post = postorder[idx+1: len(postorder)-1]
        left_pre = preorder[1: len(left_post)+1]
        right_pre = preorder[len(left_post)+1:]
        root.left = self.constructFromPrePost(left_pre, left_post)
        root.right = self.constructFromPrePost(right_pre, right_post)
        return root
