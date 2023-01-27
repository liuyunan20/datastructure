from typing import Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        def get_inorder(node):
            in_tree = []
            if not node:
                return in_tree
            in_tree += get_inorder(node.left)
            in_tree.append(node)
            in_tree += get_inorder(node.right)
            return in_tree
        tree = get_inorder(root)
        for i in range(len(tree)):
            if tree[i] == p:
                if i == len(tree) - 1:
                    return None
                return tree[i + 1]
