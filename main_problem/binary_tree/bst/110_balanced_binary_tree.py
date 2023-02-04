class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def get_depth(node):
            if not node:
                return 0
            queue = [node]
            depth = 0
            while queue:
                l = len(queue)
                depth += 1
                for _ in range(l):
                    node = queue.pop(0)
                    if node.right:
                        queue.append(node.right)
                    if node.left:
                        queue.append(node.left)
            return depth
        queue = [root]
        while queue:
            root = queue.pop(0)
            if root and abs(get_depth(root.left) - get_depth(root.right)) > 1:
                return False
            if root.left:
                queue.append(root.left)
            if root.right:
                queue.append(root.right)
        return True
