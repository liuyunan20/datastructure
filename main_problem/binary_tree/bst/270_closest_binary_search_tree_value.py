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

    def closestValue_iterator(self, root: Optional[TreeNode], target: float) -> int:
        stack = [root]
        tree = []
        while stack:
            node = stack.pop()
            if not node.left and not node.right:
                if len(tree) == 1 and tree[0] >= target:
                    return tree[0]
                if tree and tree[-1] <= target <= node.val:
                    if target - tree[-1] < node.val - target:
                        return tree[-1]
                    return node.val
                tree.append(node.val)
            else:
                if node.right:
                    stack.append(node.right)
                    node.right = None
                stack.append(node)
                if node.left:
                    stack.append(node.left)
                    node.left = None
        return tree[-1]
