from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        def get_inorder(root):
            tree = []
            if not root:
                return tree
            tree += get_inorder(root.left)
            tree.append(root.val)
            tree += get_inorder(root.right)
            return tree
        inorder_tree = get_inorder(root)
        diff = abs(target - inorder_tree[0])
        for i, val in enumerate(inorder_tree):
            if diff < abs(target - val):
                return inorder_tree[i - 1]
            diff = abs(target - val)
        return inorder_tree[-1]
