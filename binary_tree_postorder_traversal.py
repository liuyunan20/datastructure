from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # recursion solution
    def postorderTraversal_1(self, root: Optional[TreeNode]) -> List[int]:
        postorder_tree = []
        if root:
            postorder_tree += self.postorderTraversal_1(root.left)
            postorder_tree += self.postorderTraversal_1(root.right)
            postorder_tree.append(root.val)
        return postorder_tree

    # stack solution
    def postorderTraversal_2(self, root: Optional[TreeNode]) -> List[int]:
        postorder_tree = []
        my_stack = [root]
        if root:
            while my_stack:
                node = my_stack.pop()
                if not node.left and not node.right:
                    postorder_tree.append(node.val)
                else:
                    my_stack.append(node)
                    if node.right:
                        my_stack.append(node.right)
                    if node.left:
                        my_stack.append(node.left)
                    node.left = None
                    node.right = None

        return postorder_tree
