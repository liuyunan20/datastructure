# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        subtrees = {}
        def traversal(node):
            tree = ''
            if node is None:
                return 'None'
            tree += str(node.val) + ' '
            tree += traversal(node.left) + ' '
            tree += traversal(node.right) + ' '
            subtrees.setdefault(tree, [])
            subtrees[tree].append(node)
            return tree

        traversal(root)
        result = []
        for subtree in subtrees:
            if len(subtrees[subtree]) >= 2:
                result.append(subtrees[subtree][0])
        return result
