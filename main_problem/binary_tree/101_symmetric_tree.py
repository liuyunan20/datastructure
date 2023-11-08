import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        nodes = [root]
        while nodes:
            l = len(nodes)
            level = []
            for _ in range(l):
                node = nodes.pop(0)
                if node:
                    level.append(node.val)
                else:
                    level.append(-101)
                if node and node.left:
                    nodes.append(node.left)
                elif node and not node.left:
                    nodes.append(None)
                if node and node.right:
                    nodes.append(node.right)
                elif node and not node.right:
                    nodes.append(None)
            i = 0
            j = l - 1
            while i < j:
                if level[i] != level[j]:
                    return False
                i += 1
                j -= 1
        return True
