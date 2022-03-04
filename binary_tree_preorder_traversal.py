from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # recursion solution
    def preorderTraversal_1(self, root: Optional[TreeNode]) -> List[int]:
        preorder_tree = []
        if root:
            preorder_tree.append(root.val)
            preorder_tree += self.preorderTraversal(root.left)
            preorder_tree += self.preorderTraversal(root.right)
        return preorder_tree

    # iterative solution
    def preorderTraversal_2(self, root: Optional[TreeNode]) -> List[int]:
        my_stack = [root]
        preorder_tree = []
        if root:
            while my_stack:
                node = my_stack.pop()
                preorder_tree.append(node.val)
                if node.right:
                    my_stack.append(node.right)
                if node.left:
                    my_stack.append(node.left)

        return preorder_tree
