# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        nums = []
        def get_num(node, num):
            if not node.left and not node.right:
                nums.append(int(str(num) + str(node.val)))
                return
            if node.left:
                get_num(node.left, int(str(num) + str(node.val)))
            if node.right:
                get_num(node.right, int(str(num) + str(node.val)))
        get_num(root, 0)
        return sum(nums)
