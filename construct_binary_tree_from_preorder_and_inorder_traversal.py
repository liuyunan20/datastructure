from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not inorder and not preorder:
            return None
        root = TreeNode()
        root.val = preorder[0]
        i = inorder.index(root.val)  # index of root in inorder
        inorder_left = inorder[:i]
        if i == len(inorder) - 1:
            inorder_right = []
            preorder_right = []
            preorder_left = preorder[1:]
        else:
            inorder_right = inorder[i + 1:]
            left_len = len(inorder_left)
            preorder_left = preorder[1:left_len + 1]
            preorder_right = preorder[left_len + 1: len(preorder)]
        root.left = self.buildTree(preorder_left, inorder_left)
        root.right = self.buildTree(preorder_right, inorder_right)
        return root
