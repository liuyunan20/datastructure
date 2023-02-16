from typing import Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        tree = []
        nodes = [root]
        while nodes:
            current = ""
            for _ in range(len(nodes)):
                node = nodes.pop(0)
                if not node:
                    current += "# "
                else:
                    current += str(node.val) + " "
                    nodes.append(node.left)
                    nodes.append(node.right)
            tree.append(current)
        return ",".join(tree)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        print(data)
        if data == "# ":
            return None
        tree = data.split(",")
        print(tree)
        val = int(tree.pop(0))
        root = TreeNode(val)
        pre_level = [root]
        while tree:
            current = tree.pop(0).rstrip()
            current = current.split(" ")
            cur_level = []
            for node in pre_level:
                if node:
                    left = current.pop(0)
                    right = current.pop(0)
                    node.left = TreeNode(int(left)) if left != "#" else None
                    node.right = TreeNode(int(right)) if right != "#" else None
                    cur_level.append(node.left)
                    cur_level.append(node.right)
            pre_level = cur_level
        return root

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
