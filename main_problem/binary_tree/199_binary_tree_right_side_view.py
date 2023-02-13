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
        tree = []
        nodes = [root]
        while nodes:
            current_level = []
            for _ in range(len(nodes)):
                node = nodes.pop(0)
                current_level.append(node.val)
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
            tree.append(current_level)
        print(tree)
        return [x[-1] for x in tree]
