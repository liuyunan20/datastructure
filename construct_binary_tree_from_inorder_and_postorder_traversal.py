from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder and not postorder:
            return None
        root = TreeNode()
        root.val = postorder[-1]
        i = inorder.index(root.val)  # index of root in inorder
        inorder_left = inorder[:i]
        if i == len(inorder) - 1:
            inorder_right = []
            postorder_right = []
            postorder_left = postorder[:len(postorder) - 1]
        else:
            inorder_right = inorder[i + 1:]
            left_len = len(inorder_left)
            postorder_left = postorder[:left_len]
            postorder_right = postorder[left_len: len(postorder) - 1]
        root.left = self.buildTree(inorder_left, postorder_left)
        root.right = self.buildTree(inorder_right, postorder_right)
        return root
