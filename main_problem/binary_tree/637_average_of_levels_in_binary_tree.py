# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        nodes = [root]
        result = []
        while nodes:
            l = len(nodes)
            s = 0
            for _ in range(l):
                node = nodes.pop(0)
                s += node.val
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
            result.append(s/l)
        return result
