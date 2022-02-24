from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        postorder_tree = []
        if root:
            postorder_tree += self.postorderTraversal(root.left)
            postorder_tree += self.postorderTraversal(root.right)
            postorder_tree.append(root.val)
        return postorder_tree
