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
        right = []
        while nodes:
            n = len(nodes)
            for _ in range(n):
                node = nodes.pop(0)
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
            right.append(node.val)
        return right
