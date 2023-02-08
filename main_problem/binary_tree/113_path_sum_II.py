class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []

        def helper(node, target, path):
            if not node:
                return
            if not node.left and not node.right:
                if node.val == target:
                    path.append(node.val)
                    result.append(path)
                return
            else:
                target -= node.val
                path.append(node.val)
                new_path = [x for x in path]
                helper(node.left, target, new_path)
                new_path = [x for x in path]
                helper(node.right, target, new_path)

        helper(root, targetSum, [])
        return result
