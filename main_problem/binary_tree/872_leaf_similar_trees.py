class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def leafs(node):
            leaf = []
            if not node.left and not node.right:
                return [node.val]
            leaf += leafs(node.left) if node.left else []
            leaf += leafs(node.right) if node.right else []
            return leaf
        print(leafs(root1))
        print(leafs(root2))
        return leafs(root1) == leafs(root2)
