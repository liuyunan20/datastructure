from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not postorder:
            return None
        root_val = postorder[-1]
        root = TreeNode(root_val)
        idx = inorder.index(root_val)
        left_in = inorder[:idx]
        right_in = inorder[idx + 1:]
        length_right = len(right_in)
        length_left = len(left_in)
        left_post = postorder[:length_left]
        right_post = postorder[length_left:length_left + length_right]
        root.left = self.buildTree(left_in, left_post)
        root.right = self.buildTree(right_in, right_post)
        return root
