# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        def inorder_tree(root: TreeNode) -> TreeNode:
            tree = []
            if root:
                tree += inorder_tree(root.left)
                tree.append(root)
                tree += inorder_tree(root.right)
            return tree

        in_tree = inorder_tree(root)
        for i, node in enumerate(in_tree):
            if node == p:
                if i == len(in_tree) - 1:
                    return None
                return in_tree[i + 1]
