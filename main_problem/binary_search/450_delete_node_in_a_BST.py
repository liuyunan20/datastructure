class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def find_left(parent, node):
            if not node.left:
                return parent, node
            return find_left(node.left)

        def delete(parent, node, key):
            if not node:
                return
            if node.val == key:
                if not node.right:
                    parent.left = node.left
                    return
                left_p, left = find_left(node, node.right)
                if left.right:
                    left_p.left = left.right
                parent.left = left
                if node.right != left:
                    left.right = node.right
                left.left = node.left
                return
            if key > node.val:
                delete(node, node.right, key)
            if key < node.val:
                delete(node, node.left, key)

        pre = TreeNode()
        pre.left = root
        delete(pre, root, key)
        return pre.left
