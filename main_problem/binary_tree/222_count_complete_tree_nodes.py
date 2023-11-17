class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def get_tree(node):
            tree = []
            if not node:
                return tree
            tree.append(node.val)
            tree += get_tree(node.left)
            tree += get_tree(node.right)
            return tree
        return len(get_tree(root))
