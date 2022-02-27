# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root:
            if root.val == val:
                return root
            node1 = self.searchBST(root.left, val)
            node2 = self.searchBST(root.right, val)
            if node1:
                return node1
            if node2:
                return node2
        return None
