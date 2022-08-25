# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):

        def build_inorder_tree(root):
            tree = []
            if not root:
                return []
            tree += build_inorder_tree(root.left)
            tree.append(root.val)
            tree += build_inorder_tree(root.right)
            return tree

        self.tree = build_inorder_tree(root)
        self.pointer = 0

    def next(self) -> int:
        self.pointer += 1
        return self.tree[self.pointer - 1]

    def hasNext(self) -> bool:
        return self.pointer < len(self.tree)
