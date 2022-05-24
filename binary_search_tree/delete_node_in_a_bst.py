# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root:
            if root.val == key:
                if root.left and root.right:
                    pointer = root
                    successor = root.right
                    if not successor.left:
                        root.val = successor.val
                        pointer.right = successor.right
                        return root
                    while successor.left:
                        pointer = successor
                        successor = successor.left
                    root.val = successor.val
                    pointer.left = successor.right
                    return root
                elif root.left:
                    return root.left
                elif root.right:
                    return root.right
                else:
                    return None
            if root.val > key:
                root.left = self.deleteNode(root.left, key)
            if root.val < key:
                root.right = self.deleteNode(root.right, key)
        return root
