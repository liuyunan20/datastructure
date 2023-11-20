# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        tree = [root]
        result = []
        while tree:
            l = len(tree)
            level = []
            for _ in range(l):
                node = tree.pop(0)
                level.append(node.val)
                if node.left:
                    tree.append(node.left)
                if node.right:
                    tree.append(node.right)
            result.append(level)
        return result
