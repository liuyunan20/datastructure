from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def get_tree(node):
            tree = []
            if not node:
                return []
            tree.append(node)
            tree += get_tree(node.left)
            tree += get_tree(node.right)
            return tree
        whole_tree = get_tree(root)
        if not whole_tree:
            return None
        for i in range(len(whole_tree) - 1):
            whole_tree[i].right = whole_tree[i + 1]
            whole_tree[i].left = None
        whole_tree[-1].right = None
