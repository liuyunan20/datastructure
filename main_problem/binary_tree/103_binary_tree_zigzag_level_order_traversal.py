# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
        nodes = [root]
        odd = True
        while nodes:
            l = len(nodes)
            level = []
            for _ in range(l):
                node = nodes.pop(0)
                level.append(node.val)
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
            if odd:
                result.append(level)
            else:
                result.append(level[::-1])
            odd = not odd
        return result
