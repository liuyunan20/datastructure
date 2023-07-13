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
            return find_left(node, node.left)

        def delete(parent, node, key, direct):
            if not node:
                return
            if node.val == key:
                if not node.right:
                    if direct == 0:
                        parent.left = node.left
                    else:
                        parent.right = node.right
                    if parent.right == node:
                        parent.right = None
                    return
                left_p, left = find_left(node, node.right)
                if left_p != node:
                    left_p.left = left.right
                if direct == 0:
                    parent.left = left
                else:
                    parent.right = left
                left.left = node.left
                if node.right != left:
                    left.right = node.right
                return
            if key > node.val:
                delete(node, node.right, key, 1)
            if key < node.val:
                delete(node, node.left, key, 0)

        pre = TreeNode()
        pre.left = root
        delete(pre, root, key, 0)
        return pre.left
