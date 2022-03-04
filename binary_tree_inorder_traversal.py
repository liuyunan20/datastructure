from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # recursion solution
    def inorderTraversal_1(self, root: Optional[TreeNode]) -> List[int]:
        inorder_tree = []
        if root:
            inorder_tree += self.inorderTraversal(root.left)
            inorder_tree.append(root.val)
            inorder_tree += self.inorderTraversal(root.right)
        return inorder_tree

    # stack solution
    def inorderTraversal_2(self, root: Optional[TreeNode]) -> List[int]:
        inorder_tree = []
        my_stack = [root]
        if root:
            while my_stack:
                node = my_stack.pop()
                if not node.left and not node.right:
                    inorder_tree.append(node.val)
                else:
                    if node.right:
                        my_stack.append(node.right)
                    my_stack.append(node)
                    if node.left:
                        my_stack.append(node.left)
                    node.left = None
                    node.right = None
        return inorder_tree
