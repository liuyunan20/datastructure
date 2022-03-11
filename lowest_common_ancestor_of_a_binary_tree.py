class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # exceed time limit
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        current_node = root
        while len(self.find_nodes(current_node, p, q)) == 2:
            if len(self.find_nodes(current_node.left, p, q)) == 2:
                current_node = current_node.left
                continue
            elif len(self.find_nodes(current_node.right, p, q)) == 2:
                current_node = current_node.right
                continue
            else:
                return current_node


    def find_nodes(self, root, p, q):
        result = []
        if root:
            if root.val == p.val:
                result.append(root)
            if root.val == q.val:
                result.append(root)
            result += self.find_nodes(root.left, p, q)
            result += self.find_nodes(root.right, p, q)
        return result
