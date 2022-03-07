from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        count = 0
        if not root.left and not root.right:
            count += 1
        elif self.is_unival_subtree(root, root.val):
            count += 1
        count += self.countUnivalSubtrees(root.left)
        count += self.countUnivalSubtrees(root.right)
        return count

    def is_unival_subtree(self, root, val):
        if not root:
            return True
        if not root.left and not root.right and root.val == val:
            return True
        return root.val == val and self.is_unival_subtree(root.left, val) and self.is_unival_subtree(root.right, val)
