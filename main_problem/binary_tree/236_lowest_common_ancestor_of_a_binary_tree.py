class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def find_p(node, target):
            if not node:
                return False
            if node == target:
                return True
            return find_p(node.left, target) or find_p(node.right, target)

        child_parent = {}
        nodes = [root]
        p_parents = []
        q_parents = []
        while nodes:
            node = nodes.pop(0)
            if node == p and find_p(node, q):
                return p
            if node == q and find_p(node, p):
                return q
            if node == p:
                while p != root:
                    p_parents.append(child_parent[p])
                    p = child_parent[p]
            if node == q:
                while q != root:
                    q_parents.append(child_parent[q])
                    q = child_parent[q]
            if p == root and q == root:
                break
            if node.left:
                child_parent[node.left] = node
                nodes.append(node.left)
            if node.right:
                child_parent[node.right] = node
                nodes.append(node.right)
        result = root
        print(p_parents)
        print(q_parents)
        while True:
            if not p_parents or not q_parents:
                return result
            p = p_parents.pop()
            q = q_parents.pop()
            if p != q:
                return result
            else:
                result = p
