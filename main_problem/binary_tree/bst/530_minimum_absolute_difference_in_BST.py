# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def get_tree(node):
            if not node:
                return []
            tree = []
            tree += get_tree(node.left)
            tree.append(node.val)
            tree += get_tree(node.right)
            return tree
        bst = get_tree(root)
        result = bst[-1]
        for i in range(len(bst) - 1):
            result = min(result, bst[i + 1] - bst[i])
        return result
