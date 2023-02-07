class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        def bst(node):
            tree = []
            stack = [node]
            visited = set()
            while stack:
                node = stack.pop()
                if (not node.left and not node.right) or node in visited:
                    tree.append(node.val)
                else:
                    if node.right:
                        stack.append(node.right)

                    stack.append(node)
                    if node.left:
                        stack.append(node.left)
                    visited.add(node)
            for i, val in enumerate(tree):
                if i < len(tree) - 1 and val >= tree[i + 1]:
                    return 0
            return len(tree)

        if not root:
            return 0
        queue = [root]
        result = []
        while queue:
            root = queue.pop(0)
            n = bst(root)
            if n:
                result.append(n)
            else:
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
        if result:
            return max(result)
        return 0
