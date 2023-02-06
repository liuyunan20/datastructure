import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        queue = [[root]]
        tree = [[root.val]]
        while queue:
            current = queue.pop()
            next_level = []
            next_level_val = []
            for node in current:
                if node:
                    next_level.append(node.left)
                    next_level.append(node.right)
                    next_level_val.append(node.left.val) if node.left else next_level_val.append(None)
                    next_level_val.append(node.right.val) if node.right else next_level_val.append(None)
            if next_level:
                tree.append(next_level_val)
                queue.append(next_level)
        print(tree)
        for level in tree:
            i = 0
            j = len(level) - 1
            while i < j:
                if level[i] != level[j]:
                    return False
                i += 1
                j -= 1
        return True
