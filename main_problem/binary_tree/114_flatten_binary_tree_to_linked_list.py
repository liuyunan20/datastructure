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
        if not root:
            return None
        tree = []
        nodes = [root]
        while nodes:
            node = nodes.pop()
            if not node.left and not node.right:
                tree.append(node)
                continue
            if node.right:
                nodes.append(node.right)
                node.right = None
            if node.left:
                nodes.append(node.left)
                node.left = None
            nodes.append(node)
        for i in range(len(tree) - 1):
            tree[i].right = tree[i + 1]
