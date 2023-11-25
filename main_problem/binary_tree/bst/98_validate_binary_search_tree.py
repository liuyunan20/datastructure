class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def get_tree(node):
            if not node:
                return []
            tree = []
            if node.left:
                tree += get_tree(node.left)
            tree.append(node.val)
            if node.right:
                tree += get_tree(node.right)
            return tree

        bst = get_tree(root)
        for i in range(len(bst) - 1):
            if bst[i] >= bst[i + 1]:
                return False
        return True
