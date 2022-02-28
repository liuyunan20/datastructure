# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root:
            left_sub_tree = self.sub_tree(root.left)
            right_sub_tree = self.sub_tree(root.right)
            if left_sub_tree:
                for node in left_sub_tree:
                    if node.val >= root.val:
                        return False
            if right_sub_tree:
                for node in right_sub_tree:
                    if node.val <= root.val:
                        return False
            result1 = self.isValidBST(root.left)
            result2 = self.isValidBST(root.right)
            if result1 is False or result2 is False:
                return False
            return True

    def sub_tree(self, root: Optional[TreeNode]) -> list:
        sub_tree = []
        if root:
            sub_tree.append(root)
            sub_tree += self.sub_tree(root.left)
            sub_tree += self.sub_tree(root.right)
        return sub_tree
