# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        def get_tree(root):
            tree = []
            if root:
                tree += get_tree(root.left)
                tree.append(root.val)
                tree += get_tree(root.right)
            return tree
        self.tree = get_tree(root)
        self.pointer = -1

    def next(self) -> int:
        if self.pointer + 1 < len(self.tree):
            self.pointer += 1
            return self.tree[self.pointer]

    def hasNext(self) -> bool:
        if self.pointer + 1 < len(self.tree):
            return True
        return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
