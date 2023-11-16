# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        def get_tree(node):
            if not node:
                return []
            tree = []
            tree += get_tree(node.left)
            tree.append(node.val)
            tree += get_tree(node.right)
            return tree
        self.bst = get_tree(root)
        self.pointer = -1
        print(self.bst)

    def next(self) -> int:
        if self.pointer < len(self.bst) - 1:
            self.pointer += 1
            return self.bst[self.pointer]

    def hasNext(self) -> bool:
        return self.pointer < len(self.bst) - 1


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
