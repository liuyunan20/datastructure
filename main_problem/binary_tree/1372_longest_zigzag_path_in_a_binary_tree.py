class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def helper(node, dct):
            if not node:
                return 0

            if dct == 'r':
                return helper(node.left, 'l') + 1
            if dct == 'l':
                return helper(node.right, 'r') + 1

        nodes = [(root.left, 'l'), (root.right, 'r')]
        result = 0
        while nodes:
            l = len(nodes)
            for _ in range(l):
                node, dct = nodes.pop(0)
                result = max(result, helper(node, dct))
                if node and node.left:
                    nodes.append((node.left, 'l'))
                if node and node.right:
                    nodes.append((node.right, 'r'))
        return result
