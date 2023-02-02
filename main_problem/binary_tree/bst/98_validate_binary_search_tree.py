class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = [root]
        tree = []
        while stack:
            node = stack.pop()
            if not node.left and not node.right:
                if tree and tree[-1] >= node.val:
                    return False
                tree.append(node.val)
            else:
                if node.right:
                    stack.append(node.right)
                    node.right = None
                stack.append(node)
                if node.left:
                    stack.append(node.left)
                    node.left = None
        return True
