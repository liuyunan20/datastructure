# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        current_level = [root]
        data = []
        while any(current_level):
            next_level = []
            for node in current_level:
                if node:
                    data.append(str(node.val))
                    next_level.append(node.left)
                    next_level.append(node.right)
                else:
                    data.append("")
            current_level = next_level
        return ",".join(data)


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        tree = data.split(",")
        root = TreeNode(tree[0])
        tree.pop(0)
        current_level_nodes = [root]
        while tree:
            next_level_nodes = []
            for node in current_level_nodes:
                left_child = TreeNode(0)
                right_child = TreeNode(0)
                if tree[0]:
                    left_child.val = tree[0]
                else:
                    left_child = None
                tree.pop(0)
                if tree[0]:
                    right_child.val = tree[0]
                else:
                    right_child = None
                tree.pop(0)
                node.left = left_child
                node.right = right_child
                if left_child:
                    next_level_nodes.append(left_child)
                if right_child:
                    next_level_nodes.append(right_child)
            current_level_nodes = next_level_nodes
        return root



# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
