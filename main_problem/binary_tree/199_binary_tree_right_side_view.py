from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) ->List[int]:
        if not root:
            return []
        nodes = [root]
        result = []
        while nodes:
            l = len(nodes)
            result.append(nodes[-1].val)
            for _ in range(l):
                node = nodes.pop(0)
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
        return result
